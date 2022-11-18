import { hydrate, render } from "react-dom";
import App from "./App.js"

const rootElement = document.getElementById("root");
if (rootElement.hasChildNodes()) {
  hydrate(<App></App>, rootElement);
} else {
  render(<App />, rootElement);
}