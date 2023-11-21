import "./App.css"
import CentralPanel from "./CentralPanel.js"
import { CentralRightPanel } from "./CentralRightPanel.js"
import KPI from "./KPI.js"
import LeftLower from "./LeftLower.js"
import { MainPanel } from "./MainPanel.js"
import PU56 from "./PU56.js"
import RightLower from "./RightLower.js"
import CentralUpper from "./center_upper.jpg"

export default function App() {
    return <svg width={"2000mm"} height={"2000mm"} viewBox="0 0 20000 20000">
        <MainPanel></MainPanel>
        <g transform="translate(6240,960)">
            <g transform="translate(-390,-800)">
                <g transform="scale(2.2)">
                    <image opacity={1} href={CentralUpper}></image>
                </g>
            </g>
            <g transform="translate(-3100,2000)">
                <KPI></KPI>
            </g>
            <CentralPanel></CentralPanel>
            <g transform="translate(400,-900)">
                <PU56></PU56>
            </g>
            <g transform="translate(3842,0)">
                <CentralRightPanel></CentralRightPanel>
            </g>
        </g>
        <g transform="translate(1850,4050)">
            <LeftLower></LeftLower>
        </g>
        <g transform="translate(11420,4050)">
            <RightLower></RightLower>
        </g>
    </svg>
}