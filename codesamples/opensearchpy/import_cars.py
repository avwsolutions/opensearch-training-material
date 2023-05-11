from opensearchpy import OpenSearch
import opensearch_py_ml as oml

host = 'localhost'
port = 9200
auth = ('admin', 'admin') # For testing only. Don't store credentials in code.
#ca_certs_path = '/full/path/to/root-ca.pem' # Provide a CA bundle if you use intermediate CAs with your root CA.

# Optional client certificates if you don't want to use HTTP basic authentication.
#client_cert_path = '/full/path/to/client.pem'
#client_key_path = '/full/path/to/client-key.pem'

# Create the client with SSL/TLS enabled, but hostname verification disabled.
client = OpenSearch(
    hosts = [{'host': host, 'port': port}],
    http_compress = True, # enables gzip compression for request bodies
    http_auth = auth,
    use_ssl = True,
    verify_certs = False,
    ssl_assert_hostname = False,
    ssl_show_warn = False,
)

client.indices.exists(index="cars")

df = oml.csv_to_opensearch("dataset/cars.csv",
                     os_client=client,
                     os_dest_index='cars',
                     os_if_exists='replace',
                     os_dropna=True,
                     os_refresh=True,
                     index_col=0)
