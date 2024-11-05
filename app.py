from src.application import Application

def main():
    app = Application(
        width=800,
        height=600,
        fps=60,
        caption="Black Jack",
    )
    app.init()
    app.run()
    app.exit()

if __name__ == "__main__":
    main()
