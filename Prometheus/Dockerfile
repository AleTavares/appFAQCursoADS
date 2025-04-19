# Use a imagem oficial do Prometheus
FROM prom/prometheus:latest

# Copie o arquivo de configuração para o diretório padrão do Prometheus
COPY prometheus.yml /etc/prometheus/prometheus.yml

# Exponha a porta padrão do Prometheus
EXPOSE 9090

# Comando para iniciar o Prometheus com o arquivo de configuração
CMD ["--config.file=/etc/prometheus/prometheus.yml"]