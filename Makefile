CC = python3
CFLAGS = -m mwb

DEBUG =

TARGET = /usr/share/nginx/midl2021

HOST = kervadec.science:perso/midl2021
PORT = 484

.PHONY: clean generate deploy FORCE

all: generate $(TARGET)


# papers_time.json: papers.json pages/scientific-program.template
# 	$(CC) fill_times.py $^ $@

generate: pages/papers/paper.template papers.json
	$(CC) generate_papers.py $^ pages/ static/

# # pages/program/full-papers.md: pages/program/full-papers.template papers.json
# # 	$(CC) fill_template.py $^ full $@
# # pages/program/short-papers.md: pages/program/short-papers.template papers.json
# # 	$(CC) fill_template.py $^ short $@
pages/dumb_list.md: pages/dumb_list.template papers.json
	$(CC) fill_template.py $^ $@

$(TARGET): FORCE pages/dumb_list.md
	rm -rf $@
	$(CC) $(CFLAGS) . $@ $(DEBUG)
# 	chmod -R +x $@

deploy:
	rsync -rv $(TARGET) $(HOST)

clean:
	rm -rf $(TARGET)

FORCE: