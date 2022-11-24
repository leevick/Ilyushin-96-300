// import "./center.jpg" as CentralPanelBackgroud;

import center from "./center.jpg"

export default function CentralPanel() {
    return <svg xmlns="http://www.w3.org/2000/svg" version="1.1" width={800} height={"800"} viewBox="-400 -400 800 800" id="CentralPanel">
        <image x={-400} y={-400} width={800} height={800} href={center} />
    </svg>
}