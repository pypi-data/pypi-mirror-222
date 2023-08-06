from inewave.nwlistop.modelos.blocos.submercado import Submercado
from inewave.nwlistop.modelos.merclsin import MerclAnos

from inewave.nwlistop.modelos.arquivos.arquivosubmercado import (
    ArquivoSubmercado,
)

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class Mercl(ArquivoSubmercado):
    """
    Armazena os dados das saídas referentes ao mercado líquido
    de cada estágio em cada série por submercado.

    Esta classe lida com as informações de saída fornecidas pelo
    NWLISTOP e reproduzidas nos `mercl001.out`.
    """

    BLOCKS = [
        Submercado,
        MerclAnos,
    ]

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="mercl001.out"
    ) -> "Mercl":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))
