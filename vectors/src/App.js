import "./App.css"
import CentralPanel from "./CentralPanel.js"

const instruments = [new CentralPanel()]
// const instruments = [<CentralPanel/>]

export default function App() {
    return instruments.map(i => (<svg width={`${i.width / 10.0}mm`} height={`${i.height / 10.0}mm`} viewBox={`${i.left} ${i.top} ${i.width} ${i.height}`}>{
        i.render()
    }</svg>))
}