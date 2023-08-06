from inewave.nwlistop.modelos.arquivos.arquivosinpatamar import (
    ArquivoSINPatamar,
)
from inewave.nwlistop.modelos.dlppdfmaxs import DLPPdfmaxAnos

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class Dlppdfmaxs(ArquivoSINPatamar):
    """
    Armazena os dados das saídas referentes à violação das restrições
    LPP de defluência máxima por patamar para o SIN.

    Esta classe lida com as informações de saída fornecidas pelo
    NWLISTOP e reproduzidas nos `dlppdfmaxs.out`.
    """

    BLOCKS = [
        DLPPdfmaxAnos,
    ]

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="dlppdfmaxs.out"
    ) -> "Dlppdfmaxs":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))
