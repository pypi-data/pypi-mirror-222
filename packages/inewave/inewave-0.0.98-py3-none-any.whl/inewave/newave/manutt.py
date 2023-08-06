from cfinterface.files.sectionfile import SectionFile
from cfinterface.components.section import Section
from typing import TypeVar, List, Type, Optional
import pandas as pd  # type: ignore

from inewave.newave.modelos.manutt import BlocoManutencaoUTE

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class Manutt(SectionFile):
    """
    Armazena os dados de entrada do NEWAVE referentes à programação
    da manutenção das usinas térmicas.

    """

    T = TypeVar("T")

    SECTIONS: List[Type[Section]] = [BlocoManutencaoUTE]

    def __init__(self, data=...) -> None:
        super().__init__(data)

    @classmethod
    def le_arquivo(cls, diretorio: str, nome_arquivo="manutt.dat") -> "Manutt":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

    def escreve_arquivo(self, diretorio: str, nome_arquivo="manutt.dat"):
        msg = (
            "O método escreve_arquivo(diretorio, nome_arquivo) será"
            + " descontinuado na versão 1.0.0 -"
            + " use o método write(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        self.write(join(diretorio, nome_arquivo))

    @property
    def manutencoes(self) -> Optional[pd.DataFrame]:
        """
        Tabela com as manutenções por usinas.

        - codigo_empresa (`int`)
        - nome_empresa (`str`)
        - codigo_usina (`int`)
        - nome_usina (`str`)
        - codigo_unidade (`int`)
        - data_inicio (`datetime`)
        - duracao (`int`)
        - potencia (`float`)

        :return: A tabela como um DataFrame
        :rtype: pd.DataFrame | None
        """
        b = self.data.get_sections_of_type(BlocoManutencaoUTE)
        if isinstance(b, BlocoManutencaoUTE):
            return b.data
        return None

    @manutencoes.setter
    def manutencoes(self, valor: pd.DataFrame):
        b = self.data.get_sections_of_type(BlocoManutencaoUTE)
        if isinstance(b, BlocoManutencaoUTE):
            b.data = valor
        else:
            raise ValueError("Campo não lido")
