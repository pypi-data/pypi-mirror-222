from cfinterface.components.section import Section
from cfinterface.components.line import Line
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.floatfield import FloatField
from typing import List, IO
import pandas as pd  # type: ignore
import numpy as np  # type: ignore

from inewave.config import MAX_REES, MESES_DF


class BlocoEafPast(Section):
    """
    Bloco de informações de vazões passadas
    por REE, existentes no arquivo `eafpast.dat`
    do NEWAVE.
    """

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__linha = Line(
            [IntegerField(4, 0), LiteralField(10, 5)]
            + [FloatField(11, 15 + 11 * i, 2) for i in range(len(MESES_DF))]
        )
        self.__cabecalhos: List[str] = []

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoEafPast):
            return False
        bloco: BlocoEafPast = o
        if not all(
            [
                isinstance(self.data, pd.DataFrame),
                isinstance(o.data, pd.DataFrame),
            ]
        ):
            return False
        else:
            return self.data.equals(bloco.data)

    # Override
    def read(self, file: IO, *args, **kwargs):
        def converte_tabela_em_df() -> pd.DataFrame:
            cols = ["codigo_ree"] + MESES_DF
            df = pd.DataFrame(
                tabela,
                columns=cols,
            )
            df["nome_ree"] = rees
            df = df.astype({"codigo_ree": "int64"})
            df = df[["codigo_ree", "nome_ree"] + MESES_DF]
            return df

        # Salta as linhas adicionais
        for _ in range(2):
            self.__cabecalhos.append(file.readline())

        i = 0
        tabela = np.zeros((MAX_REES, len(MESES_DF) + 1))
        rees: List[str] = []
        while True:
            linha = file.readline()
            # Confere se terminaram as usinas
            if len(linha) < 3:
                # Converte para df e salva na variável
                if i > 0:
                    tabela = tabela[:i, :]
                    self.data = converte_tabela_em_df()
                break
            dados = self.__linha.read(linha)
            tabela[i, 0] = dados[0]
            rees.append(dados[1])
            tabela[i, 1:] = dados[2:]
            i += 1

    # Override
    def write(self, file: IO, *args, **kwargs):
        for linha in self.__cabecalhos:
            file.write(linha)
        if not isinstance(self.data, pd.DataFrame):
            raise ValueError(
                "Dados do eafpast.dat não foram lidos com sucesso"
            )

        for _, lin in self.data.iterrows():
            file.write(self.__linha.write(lin.tolist()))
