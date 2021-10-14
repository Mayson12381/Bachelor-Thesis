from csgo.parser import DemoParser

demo_parser = DemoParser(demofile="example.dem", demo_id="example_demo1", parse_rate=128)

data = demo_parser.parse()

data["matchID"]
data["clientName"]
data["mapName"]
data["tickRate"]
data["gameRounds"]

data_df = demo_parser.parse(return_type="df")
