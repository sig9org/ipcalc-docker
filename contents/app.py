import ipaddress
import responder

api = responder.API()


@api.route("/", static=True)
class ipcalc():
    def on_get(self, req, resp):
        resp.content = api.template('index.html')

    async def on_post(self, req, resp):
        data = await req.media()
        try:
            ip = ipaddress.ip_network(data['text'], strict=False)
            hosts = ip.num_addresses
            if hosts < 0:
                hosts = 0

            result = \
                "<table class='table table-striped'>" + \
                "<tr><th>Version</th><th>" + str(ip.version) + "</th></tr>" + \
                "<tr><th>Prefix Length</th><th>" + str(ip.prefixlen) + "</th></tr>" + \
                "<tr><th>Netmask</th><th>" + str(ip.netmask) + "</th></tr>" + \
                "<tr><th>Hostmask</th><th>" + str(ip.hostmask) + "</th></tr>" + \
                "<tr><th>Addresses</th><th>" + str(hosts) + "</th></tr>" + \
                "<tr><th>Exploded</th><th>" + str(ip.exploded) + "</th></tr>" + \
                "<tr><th>Network Address</th><th>" + str(ip.network_address) + "</th></tr>" + \
                "<tr><th>Broadcast Address</th><th>" + str(ip.broadcast_address) + "</th></tr>" + \
                "<tr><th>isMulticast</th><th>" + str(ip.is_multicast) + "</th></tr>" + \
                "<tr><th>isPrivate</th><th>" + str(ip.is_private) + "</th></tr>" + \
                "<tr><th>isLinkLocal</th><th>" + str(ip.is_link_local) + "</th></tr>" + \
                "</table>"
        except Exception as e:
            result = ''
        resp.media = {'ResultSet': '{"result": "' + result + '"}'}


if __name__ == '__main__':
    api.run(address='0.0.0.0', port=5000, debug=True)
