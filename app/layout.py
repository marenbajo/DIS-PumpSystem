def layout_config(app):
    app.geometry("800x800")
    app.grid_rowconfigure(0, weight=0)
    app.grid_rowconfigure(1, weight=1)
    app.grid_rowconfigure(2, weight=0)
    app.grid_columnconfigure(0, weight=1)
