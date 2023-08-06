"""
Este es el modulo que incluye la clase de reproductor de música
"""


class Player:
    """
    Esta clase crea un reproductor
    de música
    """
    def play(self, song):
        """
        Reproduce la cancion que recibio como parametro

        Parameters: 
        song (str): este es un string con el path de la canción

        Returns:
        int: devuelve 1 si reproduce con exito, en caso de fracaso devuelve 0
        """
        print("reproduciendo cancion")

    def stop(self):
        print("stopping")
