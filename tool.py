import os
import yaml
from jinja2 import Environment, FileSystemLoader

#---Function which exports variables from input.yaml file ---

def export_nested_yaml_variables(data, prefix=""):
   if isinstance(data, dict):
       for key, value in data.items():
           new_prefix = f"{prefix}_{key.upper()}" if prefix else key.upper()
           export_nested_yaml_variables(value, new_prefix)
   elif isinstance(data, list):
       for i, item in enumerate(data):
           new_prefix = f"{prefix}_{i}"
           export_nested_yaml_variables(item, new_prefix)
   else:
       os.environ[prefix] = str(data)
       
# Reads input.yaml file  and loads it in a variable data using safe load feature 
with open('input.yaml', 'r') as yaml_file:
   data = yaml.safe_load(yaml_file)
export_nested_yaml_variables(data)


#--------Exporting variables of non prod / acceptance  ---------------------
print("The exported environment variables are :")

print(os.environ.get('CATCHALL_DEFAULT_PORT'))
print(os.environ.get('IPFILTER_MYFILTER_0'))
print(os.environ.get('IPFILTER_MYFILTER_1'))
print(os.environ.get('IPFILTER_ALLOWALL_0'))
print(os.environ.get('IPFILTER_ALLOWALL_1'))
print(os.environ.get('APP_ACCEPTANCE_CATCHALL'))
print(os.environ.get('APP_ACCEPTANCE_FQDN_0'))
print(os.environ.get('APP_ACCEPTANCE_FQDN_1'))
print(os.environ.get('APP_ACCEPTANCE_RUNTIME_PORT'))
print(os.environ.get('APP_ACCEPTANCE_PATH_BASED_ACCESS_RESTRICTION_/_IPFILTER'))
print(os.environ.get('APP_ACCEPTANCE_PATH_BASED_ACCESS_RESTRICTION_/PUBLIC_IPFILTER'))

#--------------Prod variables ------------------------------
print(os.environ.get('APP_PRODUCTION_CATCHALL'))
print(os.environ.get('APP_PRODUCTION_FQDN_0'))
print(os.environ.get('APP_PRODUCTION_FQDN_1'))
print(os.environ.get('APP_PRODUCTION_RUNTIME_PORT'))
print(os.environ.get('APP_PRODUCTION_PATH_BASED_ACCESS_RESTRICTION_/SECRET_IPFILTER'))


#------------Render function  for jinja ----------------------

def render_nginx_template(template_path, output_path, variables):
   # Load Jinja2 environment
   env = Environment(loader=FileSystemLoader('.'))
   template = env.get_template(template_path)
   # Render the template with the provided variables
   rendered_config = template.render(**variables)
   # Write the rendered configuration to the output file
   with open(output_path, 'w') as output_file:
       output_file.write(rendered_config)
       
       
nginx_variables = {
#------------Non prod -------------------------
   'DEFAULT_PORT': os.environ.get('CATCHALL_DEFAULT_PORT'),
   'SERVER_PORT': os.environ.get('APP_ACCEPTANCE_RUNTIME_PORT'),
    'ALLOW_ALL_IPV4' : os.environ.get('IPFILTER_ALLOWALL_0'),
    'ALLOW_ALL_IPV6' : os.environ.get('IPFILTER_ALLOWALL_1'),
   'APP_ACCEPTANCE_RUNTIME_PORT': os.environ.get('APP_ACCEPTANCE_RUNTIME_PORT'),
   'APP_ACCEPTANCE_FQDN_1': os.environ.get('APP_ACCEPTANCE_FQDN_1'),
   'IPV4_CIDR_00': os.environ.get('IPFILTER_MYFILTER_0'),
   'IPV6_CIDR_01': os.environ.get('IPFILTER_MYFILTER_1'),
    'APP_PRODUCTION_FQDN_0': os.environ.get('APP_PRODUCTION_FQDN_0'),
    'APP_PRODUCTION_FQDN_1': os.environ.get('APP_PRODUCTION_FQDN_1'),
    'PROD_RUNTIME_PORT': os.environ.get('APP_PRODUCTION_RUNTIME_PORT')
   # Add more variables as needed...
}
# Replace 'nginx_template.j2' with the path to your Jinja2 template
# Replace 'nginx.conf' with the desired output path
render_nginx_template('nginx_template.j2', 'nginx.conf', nginx_variables)
