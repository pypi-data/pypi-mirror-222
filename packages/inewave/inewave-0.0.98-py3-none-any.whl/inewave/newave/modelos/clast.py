from inewave.config import MAX_UTES

from cfinterface.components.section import Section
from cfinterface.components.line import Line
from cfinterface.components.field import Field
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField
from typing import List, IO
import numpy as np  # type: ignore
import pandas as pd  # type: ignore


class BlocoUTEClasT(Section):
    """
    Bloco com informações de cargas adicionais por mês/ano
    e por subsistema.
    """

    FIM_BLOCO = " 9999"

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        campos_ute: List[Field] = [
            IntegerField(4, 1),
            LiteralField(12, 6),
            LiteralField(12, 19),
        ]
        campos_custos: List[Field] = [
            FloatField(8, 29 + 8 * i, 2) for i in range(5)
        ]
        self.__linha = Line(campos_ute + campos_custos)
        self.__cabecalhos: List[str] = []

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoUTEClasT):
            return False
        bloco: BlocoUTEClasT = o
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
        def converte_tabela_em_df():
            cols = [f"custo_{i}" for i in range(1, 6)]
            df = pd.DataFrame(tabela, columns=cols)
            df["codigo"] = codigo_ute
            df["nome"] = nome_ute
            df["tipo_combustivel"] = tipo_combustivel
            df = df[["codigo", "nome", "tipo_combustivel"] + cols]
            return df

        # Salta as linhas adicionais
        for _ in range(2):
            self.__cabecalhos.append(file.readline())

        # Variáveis auxiliares
        codigo_ute: List[int] = []
        nome_ute: List[str] = []
        tipo_combustivel: List[str] = []
        tabela = np.zeros((MAX_UTES, 5))
        i = 0
        while True:
            linha = file.readline()
            # Confere se acabou
            if len(linha) < 3:
                break
            if BlocoUTEClasT.FIM_BLOCO in linha:
                tabela = tabela[:i, :]
                self.data = converte_tabela_em_df()
                break
            dados = self.__linha.read(linha)
            tabela[i, :] = dados[3:]
            codigo_ute.append(dados[0])
            nome_ute.append(dados[1])
            tipo_combustivel.append(dados[2])
            i += 1

    # Override
    def write(self, file: IO, *args, **kwargs):
        for linha in self.__cabecalhos:
            file.write(linha)
        if not isinstance(self.data, pd.DataFrame):
            raise ValueError("Dados do c_adic.dat não foram lidos com sucesso")

        for _, linha in self.data.iterrows():
            linha_lida: pd.Series = linha
            file.write(self.__linha.write(linha_lida.tolist()))
        file.write(BlocoUTEClasT.FIM_BLOCO + "\n")


class BlocoModificacaoUTEClasT(Section):
    """
    Bloco de modificações das informações das
    usinas cadastradas no arquivo do NEWAVE `clast.dat`.
    """

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        campos_modificacao: List[Field] = [
            IntegerField(4, 1),
            FloatField(7, 8, 2),
            IntegerField(2, 17),
            IntegerField(4, 20),
            IntegerField(2, 26),
            IntegerField(4, 29),
            LiteralField(12, 35),
        ]
        self.__linha = Line(campos_modificacao)
        self.__cabecalhos: List[str] = []

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoModificacaoUTEClasT):
            return False
        bloco: BlocoModificacaoUTEClasT = o
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
        def converte_tabela_em_df():
            df = pd.DataFrame(
                data={
                    "codigo": codigo_ute,
                    "custo": custo,
                    "mes_inicio": mes_ini,
                    "ano_inicio": ano_ini,
                    "mes_fim": mes_fim,
                    "ano_fim": ano_fim,
                    "nome": nomes,
                }
            )
            return df

        # Salta as linhas adicionais
        for _ in range(2):
            self.__cabecalhos.append(file.readline())

        # Variáveis auxiliares
        codigo_ute: List[int] = []
        custo: List[float] = []
        mes_ini: List[int] = []
        ano_ini: List[int] = []
        mes_fim: List[int] = []
        ano_fim: List[int] = []
        nomes: List[str] = []
        while True:
            linha = file.readline()
            # Confere se acabou
            if len(linha) < 3:
                if len(codigo_ute) > 0:
                    self.data = converte_tabela_em_df()
                break
            dados = self.__linha.read(linha)
            codigo_ute.append(dados[0])
            custo.append(dados[1])
            mes_ini.append(dados[2])
            ano_ini.append(dados[3])
            mes_fim.append(dados[4])
            ano_fim.append(dados[5])
            nomes.append(dados[6])

    # Override
    def write(self, file: IO, *args, **kwargs):
        for linha in self.__cabecalhos:
            file.write(linha)
        if not isinstance(self.data, pd.DataFrame):
            raise ValueError("Dados do clast.dat não foram lidos com sucesso")

        for _, linha in self.data.iterrows():
            linha_lida: pd.Series = linha
            for i in [2, 3, 4, 5]:
                linha_lida[i] = (
                    None if np.isnan(linha_lida[i]) else int(linha_lida[i])
                )
            file.write(self.__linha.write(linha_lida.tolist()))
