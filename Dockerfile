FROM python:3.8-slim

ENV FLASK_APP intrepid.py

RUN apt update && apt install -y clang ninja-build cmake make python3-dev --no-install-recommends && \
    useradd -ms /bin/bash intrepid

WORKDIR /home/intrepid
USER intrepid
ENV PATH="/home/intrepid/.local/bin:${PATH}"

ADD --chown=intrepid:intrepid intrepid intrepid
ADD --chown=intrepid:intrepid intrepyd intrepyd
ADD --chown=intrepid:intrepid app app
COPY --chown=intrepid:intrepid requirements.txt Makefile setup.py setup.cfg VERSION intrepid.py docker/app.sh .pylintrc ./

RUN pip3 install -r requirements.txt && \
    mkdir -p libs/linux64/ && \
    make && \
    cp intrepid_build/_api.so libs/linux64/ && strip libs/linux64/_api.so && \
    make install_intrepyd && \
    rm -fr intrepid intrepyd intrepid_build tests setup.py setup.cfg VERSION Makefile && \
    rm -fr __pycache__ build dist intrepyd.egg-info libs requirements.txt _api.so

EXPOSE 8000
ENTRYPOINT [ "./app.sh" ]
