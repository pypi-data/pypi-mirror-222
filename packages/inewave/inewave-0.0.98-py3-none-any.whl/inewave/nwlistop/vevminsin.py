from inewave.nwlistop.modelos.arquivos.arquivosin import (
    ArquivoSIN,
)
from inewave.nwlistop.modelos.vevminsin import VevminAnos

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class Vevminsin(ArquivoSIN):
    """
    Armazena os dados das saídas referentes às violações da meta
    de energia da vazão mínima para o SIN.

    Esta classe lida com as informações de saída fornecidas pelo
    NWLISTOP e reproduzidas nos `vevminsin.out`

    """

    BLOCKS = [
        VevminAnos,
    ]

    @classmethod
    def le_arquivo(
        cls, diretorio: str, nome_arquivo="vevminsin.out"
    ) -> "Vevminsin":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))
