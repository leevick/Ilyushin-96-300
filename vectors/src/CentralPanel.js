// import "./center.jpg" as CentralPanelBackgroud;

import center_upper_texture from "./center_upper_texture.jpg"



export default function CentralPanel() {
    var scale = 4.4
    return <svg xmlns="http://www.w3.org/2000/svg" version="1.1" width={1742 * scale} height={scale * 918} viewBox={`0 0 ${scale * 1742} ${scale * 918}`} id="CentralPanel" >
        <image x={0} y={0} width={1742 * scale} height={918 * scale} href={center_upper_texture} />
        <circle cx={1025} cy={1325} r={800} fill={"white"} fillOpacity={0.5} ></circle>
    </svg >
}