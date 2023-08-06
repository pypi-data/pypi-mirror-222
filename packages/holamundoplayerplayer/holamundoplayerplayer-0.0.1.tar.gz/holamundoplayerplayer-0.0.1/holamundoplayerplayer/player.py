"""
Este es el modulo que incluye la clase
de reproductor de musica
"""


class Player:
    """
    Esta clase crea un reproductor 
    de musica
    """

    def play(self, song):
        """
        Reproduce la cancion que recibio como parametro

        Parameters:
        song (str): Este es un string con el path de la cancion

        Returns:
        int: devulve 1 si devuelve con exito, en caso de fracaso devuelve 0
        """
        print("Reproduciendo cancion")

    def stop(self):
        print("stopping")
