import "./App.css"
import CentralPanel from "./CentralPanel.js"
import KPI from "./KPI.js"
import PU56 from "./PU56.js"

export default function App() {
    return [<svg width={"160mm"} height={"160mm"} viewBox="-800 -800 1600 1600">
        <KPI></KPI>
    </svg>,
    <svg width={`${2.2 * 1742 / 10.0}mm`} height={`${2.2 * 918 / 10.0}mm`} viewBox={`0 0 ${2.2 * 1742} ${2.2 * 918}`}>
        <CentralPanel></CentralPanel>
    </svg>,
    <svg width={"470mm"} height={"80mm"} viewBox="0 0 4700 800">
        <PU56></PU56>
    </svg>
    ]
}