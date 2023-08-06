from cfinterface.files.sectionfile import SectionFile
from inewave.newave.modelos.cortes import SecaoDadosCortes

import pandas as pd  # type: ignore
from typing import TypeVar, Optional, Union, List

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class Cortes(SectionFile):
    """
    Armazena os dados de saída do NEWAVE referentes aos
    cortes de Benders.
    """

    T = TypeVar("T")

    SECTIONS = [SecaoDadosCortes]
    STORAGE = "BINARY"

    def __init__(self, data=...) -> None:
        super().__init__(data)

    @classmethod
    def le_arquivo(cls, diretorio: str, nome_arquivo="cortes.dat") -> "Cortes":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

    def escreve_arquivo(self, diretorio: str, nome_arquivo="cortes.dat"):
        msg = (
            "O método escreve_arquivo(diretorio, nome_arquivo) será"
            + " descontinuado na versão 1.0.0 -"
            + " use o método write(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        self.write(join(diretorio, nome_arquivo))

    @classmethod
    def read(
        cls,
        content: Union[str, bytes],
        tamanho_registro: int = 1664,
        indice_ultimo_corte: int = 0,
        numero_total_cortes: int = 10000,
        codigos_rees: List[int] = [],
        codigos_uhes: List[int] = [],
        codigos_submercados: List[int] = [],
        ordem_maxima_parp: int = 12,
        lag_maximo_gnl: int = 2,
        *args,
        **kwargs
    ) -> "Cortes":
        return super().read(
            content,
            tamanho_registro=tamanho_registro,
            indice_ultimo_corte=indice_ultimo_corte,
            numero_total_cortes=numero_total_cortes,
            codigos_rees=codigos_rees,
            codigos_uhes=codigos_uhes,
            codigos_submercados=codigos_submercados,
            ordem_maxima_parp=ordem_maxima_parp,
            lag_maximo_gnl=lag_maximo_gnl,
            *args,
            **kwargs
        )

    @property
    def cortes(self) -> Optional[pd.DataFrame]:
        """
        Retorna o conjunto dos cortes de Benders construídos
        durante o cálculo da política.

        - indice_corte (`int`)
        - iteracao_construcao (`str`)
        - indice_forward (`int`)
        - iteracao_inativacao (`int`)
        - rhs (`float`)

        Se o estágio em questão for agregado em REE:

        - pi_earm_ree1 (`float`)
        - pi_ena_ree1_lag1 (`float`)
        - ...
        - pi_ena_ree1_lagN (`float`)
        - pi_earm_ree2 (`float`)
        - ...
        - pi_ena_reeR_lagN (`float`)

        Se o estágio em questão for individualizado:

        - pi_varm_uhe1 (`float`)
        - pi_qafl_uhe1_lag1 (`float`)
        - ...
        - pi_qafl_uhe1_lagN (`float`)
        - pi_varm_uhe2 (`float`)
        - ...
        - pi_qafl_uheU_lagN (`float`)

        Para todos os estágios:

        - pi_gnl_sbm1_pat1_lag1 (`float`)
        - ...
        - pi_gnl_sbm1_pat1_lagL (`float`)
        - pi_gnl_sbm1_pat2_lag1 (`float`)
        - ...
        - pi_gnl_sbm1_patP_lagL (`float`)
        - pi_gnl_sbm2_pat1_lag1 (`float`)
        - ...
        - pi_gnl_sbmS_patP_lagL (`float`)

        R é o número de REEs.

        U é o número de UHEs.

        S é o número de submercados.

        N é a máxima ordem do modelo PAR(p) ajustado.

        P é o número de patamares de carga.

        L é o lag máximo de despacho GNL antecipado.

        :return: Os coeficientes dos cortes em uma tabela.
        :rtype: pd.DataFrame | None
        """
        dados = [r for r in self.data.of_type(SecaoDadosCortes)]
        if len(dados) == 1:
            return dados[0].data
        else:
            return None
