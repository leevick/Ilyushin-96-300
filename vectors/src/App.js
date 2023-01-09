import "./App.css"
import CentralPanel from "./CentralPanel.js"
import KPI from "./KPI.js"

const instruments = [new CentralPanel(), new KPI()]
// const instruments = [<CentralPanel/>]

export default function App() {
    return instruments.map(i => (<svg width={`${i.width / 10.0}mm`} height={`${i.height / 10.0}mm`} viewBox={`${i.left} ${i.top} ${i.width} ${i.height}`}>{
        i.render()
    }</svg>))
}