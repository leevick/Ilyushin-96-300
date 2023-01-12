import "./App.css"
import CentralPanel from "./CentralPanel.js"
import KPI from "./KPI.js"

export default function App() {
    return [<svg width={"160mm"} height={"160mm"} viewBox="-800 -800 1600 1600">
        <KPI></KPI>
    </svg>,
    <svg width={`${2.2 * 1742 / 10.0}mm`} height={`${2.2 * 918 / 10.0}mm`} viewBox={`0 0 ${2.2 * 1742} ${2.2 * 918}`}>
        <CentralPanel></CentralPanel>
    </svg>]
}