def handle_greet(self):
        """Handle the greet button press."""
        name = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello {name}"