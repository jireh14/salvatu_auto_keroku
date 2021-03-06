import web
import config
import json


class Api_fallas:
    def get(self, codigo_falla):
        try:
            # http://salvatuauto.herokuapp.com/api_fallas?user_hash=12345&action=get
            if codigo_falla is None:
                result = config.model.get_all_fallas()
                fallas_json = []
                for row in result:
                    tmp = dict(row)
                    fallas_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(fallas_json)
            else:
                # http://salvatuauto.herokuapp.com/api_fallas?user_hash=12345&action=get&codigo_falla=codigo_falla
                result = config.model.get_fallas(int(codigo_falla))
                fallas_json = []
                fallas_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(fallas_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            fallas_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(fallas_json)

# http://localhost:8080/api_fallas?user_hash=12345&action=put&id_falla=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self,codigo_falla,descripcion,causa,imagen,id_coche):
        try:
            config.model.insert_fallas(codigo_falla,descripcion,causa,imagen,id_coche)
            fallas_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(fallas_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_fallas?user_hash=12345&action=delete&codigo_falla=codigo_falla
    def delete(self, codigo_falla):
        try:
            config.model.delete_fallas(codigo_falla)
            fallas_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(fallas_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_fallas?user_hash=12345&action=update&id_falla=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, codigo_falla,descripcion,causa,imagen,id_coche):
        try:
            config.model.edit_fallas(codigo_falla,descripcion,causa,imagen,id_coche)
            fallas_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(fallas_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            fallas_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(fallas_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            codigo_falla=None,
            descripcion=None,
            causa=None,
            imagen=None,
            id_coche=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE

            codigo_falla=user_data.codigo_falla

            descripcion=user_data.descripcion

            causa=user_data.causa

            imagen=user_data.imagen

            id_coche=user_data.id_coche

            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(codigo_falla)
                elif action == 'put':
                    return self.put(codigo_falla,descripcion,causa,imagen,id_coche)
                elif action == 'delete':
                    return self.delete(codigo_falla)
                elif action == 'update':
                    return self.update(codigo_falla,descripcion,causa,imagen,id_coche)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
