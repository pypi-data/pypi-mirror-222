from typing import TypeVar, List, Optional, Union
from datetime import datetime

from cfinterface.files.registerfile import RegisterFile
from inewave.newave.modelos.eolicafte import RegistroEolicaFTE, RegistroPEEFTE

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class EolicaFTE(RegisterFile):
    """
    Armazena os dados de entrada do NEWAVE referentes às funções de
    transferência vento-potência.
    """

    T = TypeVar("T")

    REGISTERS = [RegistroEolicaFTE, RegistroPEEFTE]

    def __init__(self, data=...) -> None:
        super().__init__(data)

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="eolica-fte.csv"
    ) -> "EolicaFTE":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

    def escreve_arquivo(self, diretorio: str, nome_arquivo="eolica-fte.csv"):
        msg = (
            "O método escreve_arquivo(diretorio, nome_arquivo) será"
            + " descontinuado na versão 1.0.0 -"
            + " use o método write(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        self.write(join(diretorio, nome_arquivo))

    def eolica_funcao_producao(
        self,
        codigo_eolica: Optional[int] = None,
        data_inicial: Optional[datetime] = None,
        data_final: Optional[datetime] = None,
        coeficiente_linear: Optional[float] = None,
        coeficiente_angular: Optional[float] = None,
    ) -> Optional[Union[RegistroEolicaFTE, List[RegistroEolicaFTE]]]:
        """
        Obtém um registro que contém a função de produção vento-geração
        para um período de tempo.

        :param codigo_eolica: código que especifica a usina
        :type codigo_eolica: int | None
        :param data_inicial: a data inicial de validade para a função
        :type data_inicial: datetime | None
        :param data_final: a data final de validade para a função
        :type data_final: datetime | None
        :param coeficiente_linear: o coeficiente linear
        :type coeficiente_linear: float | None
        :param coeficiente_angular: o coeficiente angular
        :type coeficiente_angular: float | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroEolicaFTE` |
            list[:class:`RegistroEolicaFTE`] | None
        """
        return self.data.get_registers_of_type(
            RegistroEolicaFTE,
            codigo_eolica=codigo_eolica,
            data_inicial=data_inicial,
            data_final=data_final,
            coeficiente_linear=coeficiente_linear,
            coeficiente_angular=coeficiente_angular,
        )

    def pee_fpvp_lin_pu_per(
        self,
        codigo_pee: Optional[int] = None,
        data_inicial: Optional[datetime] = None,
        data_final: Optional[datetime] = None,
        coeficiente_linear: Optional[float] = None,
        coeficiente_angular: Optional[float] = None,
    ) -> Optional[Union[RegistroPEEFTE, List[RegistroPEEFTE]]]:
        """
        Obtém um registro que contém a função de produção vento-geração
        para um período de tempo para um PEE, em p.u.

        :param codigo_pee: código que especifica o PEE
        :type codigo_pee: int | None
        :param data_inicial: a data inicial de validade para a função
        :type data_inicial: datetime | None
        :param data_final: a data final de validade para a função
        :type data_final: datetime | None
        :param coeficiente_linear: o coeficiente linear
        :type coeficiente_linear: float | None
        :param coeficiente_angular: o coeficiente angular
        :type coeficiente_angular: float | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RegistroPEEFTE` |
            list[:class:`RegistroPEEFTE`] | None
        """
        return self.data.get_registers_of_type(
            RegistroPEEFTE,
            codigo_pee=codigo_pee,
            data_inicial=data_inicial,
            data_final=data_final,
            coeficiente_linear=coeficiente_linear,
            coeficiente_angular=coeficiente_angular,
        )
