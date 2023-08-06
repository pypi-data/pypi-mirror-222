from inewave.newave.modelos.curva import (
    BlocoConfiguracoesPenalizacaoCurva,
    BlocoPenalidadesViolacaoREECurva,
    BlocoCurvaSegurancaREE,
    BlocoMaximoIteracoesProcessoIterativoEtapa2,
    BlocoIteracaoAPartirProcessoIterativoEtapa2,
    BlocoToleranciaProcessoIterativoEtapa2,
    BlocoImpressaoRelatorioProcessoIterativoEtapa2,
)

from cfinterface.files.sectionfile import SectionFile
from typing import TypeVar, Optional
import pandas as pd  # type: ignore

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class Curva(SectionFile):
    """
    Armazena os dados de entrada do NEWAVE referentes à curva para
    penalização por volume mínimo dos reservatórios.
    """

    T = TypeVar("T")

    SECTIONS = [
        BlocoConfiguracoesPenalizacaoCurva,
        BlocoPenalidadesViolacaoREECurva,
        BlocoCurvaSegurancaREE,
        BlocoMaximoIteracoesProcessoIterativoEtapa2,
        BlocoIteracaoAPartirProcessoIterativoEtapa2,
        BlocoToleranciaProcessoIterativoEtapa2,
        BlocoImpressaoRelatorioProcessoIterativoEtapa2,
    ]

    def __init__(self, data=...) -> None:
        super().__init__(data)

    @classmethod
    def le_arquivo(cls, diretorio: str, nome_arquivo="curva.dat") -> "Curva":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

    def escreve_arquivo(self, diretorio: str, nome_arquivo="curva.dat"):
        msg = (
            "O método escreve_arquivo(diretorio, nome_arquivo) será"
            + " descontinuado na versão 1.0.0 -"
            + " use o método write(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        self.write(join(diretorio, nome_arquivo))

    @property
    def configuracoes_penalizacao(self) -> Optional[list]:
        """
        Linha de configuração das opções de penalização do
        arquivo curva.dat.

        :return: Os valores dos campos da linha como uma lista.
        :rtype: Optional[list]
        """
        b = self.data.get_sections_of_type(BlocoConfiguracoesPenalizacaoCurva)
        if isinstance(b, BlocoConfiguracoesPenalizacaoCurva):
            return b.data
        return None

    @configuracoes_penalizacao.setter
    def configuracoes_penalizacao(self, valor: list):
        b = self.data.get_sections_of_type(BlocoConfiguracoesPenalizacaoCurva)
        if isinstance(b, BlocoConfiguracoesPenalizacaoCurva):
            b.data = valor
        else:
            raise ValueError("Campo não lido")

    @property
    def custos_penalidades(self) -> Optional[pd.DataFrame]:
        """
        Tabela com os custos para penalização em cada REE.

        - ree (`int`)
        - penalidade (`float`)

        :return: Os custos por REE em um DataFrame.
        :rtype: pd.DataFrame | None
        """
        b = self.data.get_sections_of_type(BlocoPenalidadesViolacaoREECurva)
        if isinstance(b, BlocoPenalidadesViolacaoREECurva):
            return b.data
        return None

    @custos_penalidades.setter
    def custos_penalidades(self, valor: pd.DataFrame):
        b = self.data.get_sections_of_type(BlocoPenalidadesViolacaoREECurva)
        if isinstance(b, BlocoPenalidadesViolacaoREECurva):
            b.data = valor
        else:
            raise ValueError("Campo não lido")

    @property
    def curva_seguranca(self) -> Optional[pd.DataFrame]:
        """
        Tabela da curva de segurança por REE.

        - ree (`int`)
        - ano (`int`)
        - janeiro (`float`)
        - fevereiro (`float`)
        - ...
        - dezembro (`float`)

        :return: Os valores dos campos da linha como uma lista.
        :rtype: pd.DataFrame | None
        """
        b = self.data.get_sections_of_type(BlocoCurvaSegurancaREE)
        if isinstance(b, BlocoCurvaSegurancaREE):
            return b.data
        return None

    @curva_seguranca.setter
    def curva_seguranca(self, valor: pd.DataFrame):
        b = self.data.get_sections_of_type(BlocoCurvaSegurancaREE)
        if isinstance(b, BlocoCurvaSegurancaREE):
            b.data = valor
        else:
            raise ValueError("Campo não lido")

    @property
    def maximo_iteracoes_etapa2(self) -> Optional[int]:
        """
        Número máximo de iterações no processo iterativo de 2ª
        etapa.

        :return: O valor como um int
        :rtype: Optional[int]
        """
        b = self.data.get_sections_of_type(
            BlocoMaximoIteracoesProcessoIterativoEtapa2
        )
        if isinstance(b, BlocoMaximoIteracoesProcessoIterativoEtapa2):
            return b.data
        return None

    @maximo_iteracoes_etapa2.setter
    def maximo_iteracoes_etapa2(self, valor: int):
        b = self.data.get_sections_of_type(
            BlocoMaximoIteracoesProcessoIterativoEtapa2
        )
        if isinstance(b, BlocoMaximoIteracoesProcessoIterativoEtapa2):
            b.data = valor
        else:
            raise ValueError("Campo não lido")

    @property
    def iteracao_a_partir_etapa2(self) -> Optional[int]:
        """
        Iteração a partir da qual ocorre o processo iterativo de 2ª
        etapa.

        :return: O valor como um int
        :rtype: Optional[int]
        """
        b = self.data.get_sections_of_type(
            BlocoIteracaoAPartirProcessoIterativoEtapa2
        )
        if isinstance(b, BlocoIteracaoAPartirProcessoIterativoEtapa2):
            return b.data
        return None

    @iteracao_a_partir_etapa2.setter
    def iteracao_a_partir_etapa2(self, valor: int):
        b = self.data.get_sections_of_type(
            BlocoIteracaoAPartirProcessoIterativoEtapa2
        )
        if isinstance(b, BlocoIteracaoAPartirProcessoIterativoEtapa2):
            b.data = valor
        else:
            raise ValueError("Campo não lido")

    @property
    def tolerancia_processo_etapa2(self) -> Optional[float]:
        """
        Tolerância para a execução do processo iterativo de etapa 2.

        :return: O valor como um float
        :rtype: Optional[float]
        """
        b = self.data.get_sections_of_type(
            BlocoToleranciaProcessoIterativoEtapa2
        )
        if isinstance(b, BlocoToleranciaProcessoIterativoEtapa2):
            return b.data
        return None

    @tolerancia_processo_etapa2.setter
    def tolerancia_processo_etapa2(self, valor: int):
        b = self.data.get_sections_of_type(
            BlocoToleranciaProcessoIterativoEtapa2
        )
        if isinstance(b, BlocoToleranciaProcessoIterativoEtapa2):
            b.data = valor
        else:
            raise ValueError("Campo não lido")

    @property
    def impressao_relatorio_etapa2(self) -> Optional[int]:
        """
        Opção de impressão ou não do relatório do
        processo iterativo de 2ª etapa.

        :return: O valor como um int
        :rtype: Optional[int]
        """
        b = self.data.get_sections_of_type(
            BlocoImpressaoRelatorioProcessoIterativoEtapa2
        )
        if isinstance(b, BlocoImpressaoRelatorioProcessoIterativoEtapa2):
            return b.data
        return None

    @impressao_relatorio_etapa2.setter
    def impressao_relatorio_etapa2(self, valor: int):
        b = self.data.get_sections_of_type(
            BlocoImpressaoRelatorioProcessoIterativoEtapa2
        )
        if isinstance(b, BlocoImpressaoRelatorioProcessoIterativoEtapa2):
            b.data = valor
        else:
            raise ValueError("Campo não lido")
