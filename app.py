from src.application import Application

def main():
    app = Application(
        width=800,
        height=600,
        fps=10,
        caption="Black Jack",
        debug=False
    )
    app.init()
    app.run()
    app.exit()

if __name__ == "__main__":
    main()
