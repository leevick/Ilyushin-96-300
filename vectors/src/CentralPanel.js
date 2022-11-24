// import "./center.jpg" as CentralPanelBackgroud;

import center_upper_texture from "./center_upper_texture.jpg"



export default function CentralPanel() {
    var scale = 2.2
    const vbm_w = 800
    const vbm_c = 5
    const sig_w = 295
    const sig_h = 165

    return <svg xmlns="http://www.w3.org/2000/svg" version="1.1" width={1742 * scale} height={scale * 918} viewBox={`0 0 ${scale * 1742} ${scale * 918}`} id="CentralPanel" >
        <image x={0} y={0} width={1742 * scale} height={918 * scale} href={center_upper_texture} />
        <circle cx={512.5} cy={662.5} r={400} fill={"white"} fillOpacity={0.5} ></circle>
        <circle cx={2470} cy={1500} r={400} fill={"white"} fillOpacity={1.0} ></circle>
        <rect x={2065} y={250} width={vbm_w} height={vbm_w} fillOpacity={0.8}></rect>
        <rect x={820} y={1330} width={sig_w * 4} height={sig_h * 4} fillOpacity={1.0}></rect>
        <rect x={3225} y={1500} width={sig_w * 2} height={sig_h * 3} fillOpacity={1.0}></rect>
    </svg >
}