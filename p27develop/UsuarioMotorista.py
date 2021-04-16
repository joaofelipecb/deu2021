import p26struct.Usuario

class UsuarioMotorista(p26struct.Usuario.Usuario):
    def __init__(self,id):
        super().__init__(id,'UsuarioMotorista')
        
    @property
    def motorista(self):
        import p23control._Database
        self.motoristaCache = p23control._Database.get_by_id_with_cache(self.motoristaCache,'p27develop.Motorista',self.id)
        return self.motoristaCache
