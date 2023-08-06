from cfinterface.files.sectionfile import SectionFile
from cfinterface.components.section import Section
from typing import TypeVar, List, Type, Optional
import pandas as pd  # type: ignore

from inewave.newave.modelos.penalid import BlocoPenalidades

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class Penalid(SectionFile):
    """
    Armazena os dados de entrada do NEWAVE referentes às penalidades
    aplicadas por desvio.

    """

    T = TypeVar("T")

    SECTIONS: List[Type[Section]] = [BlocoPenalidades]

    def __init__(self, data=...) -> None:
        super().__init__(data)

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="penalid.dat"
    ) -> "Penalid":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

    def escreve_arquivo(self, diretorio: str, nome_arquivo="penalid.dat"):
        msg = (
            "O método escreve_arquivo(diretorio, nome_arquivo) será"
            + " descontinuado na versão 1.0.0 -"
            + " use o método write(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        self.write(join(diretorio, nome_arquivo))

    @property
    def penalidades(self) -> Optional[pd.DataFrame]:
        """
        Tabela com as penalidades.

        - mnemonico (`str`)
        - penalidade_1 (`float`)
        - penalidade_2 (`float`)
        - submercado (`int`)

        :return: A tabela como um DataFrame.
        :rtype: pd.DataFrame | None
        """
        b = self.data.get_sections_of_type(BlocoPenalidades)
        if isinstance(b, BlocoPenalidades):
            return b.data
        return None

    @penalidades.setter
    def penalidades(self, df: pd.DataFrame):
        b = self.data.get_sections_of_type(BlocoPenalidades)
        if isinstance(b, BlocoPenalidades):
            b.data = df
