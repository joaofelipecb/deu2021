import p17data.config

vincular = []

vincular.append({'usuario':{'_type':'UsuarioMotorista'},
             'geolocalizacao': None
            })

vincular.append({'motorista.restaurante':{'_sql':'''SELECT restaurante_id
                                                FROM restaurantes
                                                WHERE ST_DISTANCE(restaurante_geom, :motorista_geom) < ''' + str(p17data.config.dist15min)
                                     }
            })
