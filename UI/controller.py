import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDGenre(self):
        generi = self._model.getGeneri()

        for genere in generi:
            self._view._ddGenre.options.append(ft.dropdown.Option(genere))

    def handleGenere(self):
        genere = self._view._ddGenre.value

        if genere is None:
            self._view.txt_result.apppend(ft.TextField("selezionare un genere"), color="red")
            self._view.update_page()
            return

        self._model.getNodes(genere)

    def handleCreaGrafo(self, e):
        self.handleGenere()
        self._model.build_graph()


    def handleCreaGrafo(self,e):
        pass

    def handleCammino(self,e):
        pass