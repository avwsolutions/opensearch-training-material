FROM ghcr.io/calyptia/fluentd:v1.15-debian-1 

USER root

RUN gem install fluent-plugin-opensearch

USER fluent
ENTRYPOINT ["tini",  "--", "/bin/entrypoint.sh"]
CMD ["fluentd"]
