CC = python3
CFLAGS = -m mwb

DEBUG =

TARGET = /usr/share/nginx/midl2021

HOST = castelbrazelbub.net:

.PHONY: clean generate generate_sessions deploy FORCE

all: generate generate_sessions $(TARGET)

papers.json: long_papers.csv short_papers.csv program.html
	$(CC) csv2json.py


generate: pages/papers/paper.template papers.json
	$(CC) generate_papers.py $^ pages/ static/

generate_sessions: pages/sessions/session.template papers.json
	$(CC) generate_sessions.py $^ pages/sessions

pages/program.md: pages/program.template papers.json
	$(CC) fill_template.py $^ $@

$(TARGET): FORCE pages/program.md
	rm -rf $@
	$(CC) $(CFLAGS) . $@ $(DEBUG)
# 	chmod -R +x $@

deploy:
	rsync -rv $(TARGET) $(HOST)

clean:
	rm -rf $(TARGET)

FORCE: