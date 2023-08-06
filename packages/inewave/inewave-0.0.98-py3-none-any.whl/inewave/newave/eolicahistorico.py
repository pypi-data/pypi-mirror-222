from typing import TypeVar, List, Optional, Union
from datetime import datetime

from cfinterface.files.registerfile import RegisterFile
from inewave.newave.modelos.eolicahistorico import (
    RegistroEolicaHistoricoVentoHorizonte,
    RegistroEolicaHistoricoVento,
    RegistroHistoricoVentoHorizonte,
    RegistroHistoricoVento,
)

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class EolicaHistorico(RegisterFile):
    """
    Armazena os dados de entrada do NEWAVE referentes ao histórico
    de ventos das usinas eólicas.
    """

    T = TypeVar("T")

    REGISTERS = [
        RegistroEolicaHistoricoVentoHorizonte,
        RegistroEolicaHistoricoVento,
        RegistroHistoricoVentoHorizonte,
        RegistroHistoricoVento,
    ]

    def __init__(self, data=...) -> None:
        super().__init__(data)

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="hist-ventos.csv"
    ) -> "EolicaHistorico":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

    def escreve_arquivo(self, diretorio: str, nome_arquivo="hist-ventos.csv"):
        msg = (
            "O método escreve_arquivo(diretorio, nome_arquivo) será"
            + " descontinuado na versão 1.0.0 -"
            + " use o método write(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        self.write(join(diretorio, nome_arquivo))

    def eolica_historico_vento_horizonte(
        self,
        data_inicial: Optional[datetime] = None,
        data_final: Optional[datetime] = None,
    ) -> Optional[
        Union[
            RegistroEolicaHistoricoVentoHorizonte,
            List[RegistroEolicaHistoricoVentoHorizonte],
        ]
    ]:
        """
        Obtém um registro que contém o horizonte de um histórico.

        :param data_inicial: data de início do histórico
        :type data_inicial: datetime | None
        :param data_final: data de fim do histórico
        :type data_final: datetime | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroEolicaHistoricoVentoHorizonte` |
            list[:class:`RegistroEolicaHistoricoVentoHorizonte`] | None
        """
        return self.data.get_registers_of_type(
            RegistroEolicaHistoricoVentoHorizonte,
            data_inicial=data_inicial,
            data_final=data_final,
        )

    def eolica_historico_vento(
        self,
        codigo_eolica: Optional[int] = None,
        data_inicial: Optional[datetime] = None,
        data_final: Optional[datetime] = None,
        velocidade: Optional[float] = None,
        direcao: Optional[float] = None,
    ) -> Optional[
        Union[
            RegistroEolicaHistoricoVento,
            List[RegistroEolicaHistoricoVento],
        ]
    ]:
        """
        Obtém um registro que contém a o valor de vento para um
        intervalo do histórico.

        :param codigo_eolica: código da usina eólica
        :type codigo_eolica: int | None
        :param data_inicial: data de início do registro histórico
        :type data_inicial: datetime | None
        :param data_final: data de fim do registro histórico
        :type data_final: datetime | None
        :param velocidade: velocidade do vento
        :type velocidade: float | None
        :param direcao: direção do vento
        :type direcao: float | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroEolicaHistoricoVento` |
            list[:class:`RegistroEolicaHistoricoVento`] | None
        """
        return self.data.get_registers_of_type(
            RegistroEolicaHistoricoVento,
            codigo_eolica=codigo_eolica,
            data_inicial=data_inicial,
            data_final=data_final,
            velocidade=velocidade,
            direcao=direcao,
        )

    def vento_hist_horiz(
        self,
        data_inicial: Optional[datetime] = None,
        data_final: Optional[datetime] = None,
    ) -> Optional[
        Union[
            RegistroHistoricoVentoHorizonte,
            List[RegistroHistoricoVentoHorizonte],
        ]
    ]:
        """
        Obtém um registro que contém o horizonte de um histórico.

        :param data_inicial: data de início do histórico
        :type data_inicial: datetime | None
        :param data_final: data de fim do histórico
        :type data_final: datetime | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroHistoricoVentoHorizonte` |
            list[:class:`RegistroHistoricoVentoHorizonte`] | None
        """
        return self.data.get_registers_of_type(
            RegistroHistoricoVentoHorizonte,
            data_inicial=data_inicial,
            data_final=data_final,
        )

    def vento_hist(
        self,
        codigo_eolica: Optional[int] = None,
        data_inicial: Optional[datetime] = None,
        data_final: Optional[datetime] = None,
        velocidade: Optional[float] = None,
        direcao: Optional[float] = None,
    ) -> Optional[
        Union[
            RegistroHistoricoVento,
            List[RegistroHistoricoVento],
        ]
    ]:
        """
        Obtém um registro que contém a o valor de vento para um
        intervalo do histórico.

        :param codigo_eolica: código da usina eólica
        :type codigo_eolica: int | None
        :param data_inicial: data de início do registro histórico
        :type data_inicial: datetime | None
        :param data_final: data de fim do registro histórico
        :type data_final: datetime | None
        :param velocidade: velocidade do vento
        :type velocidade: float | None
        :param direcao: direção do vento
        :type direcao: float | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroHistoricoVento` |
            list[:class:`RegistroHistoricoVento`] | None
        """
        return self.data.get_registers_of_type(
            RegistroHistoricoVento,
            codigo_eolica=codigo_eolica,
            data_inicial=data_inicial,
            data_final=data_final,
            velocidade=velocidade,
            direcao=direcao,
        )
