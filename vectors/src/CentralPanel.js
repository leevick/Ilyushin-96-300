// import "./center.jpg" as CentralPanelBackgroud;

import center_upper_texture from "./center_upper_texture.jpg"



export default function CentralPanel() {
    var scale = 2.2
    const vbm_w = 800
    const vbm_c = 5
    const sig_w = 295
    const sig_h = 165
    const rmi_w = 800
    const rmi_h = 1150

    return <svg xmlns="http://www.w3.org/2000/svg" version="1.1" width={1742 * scale} height={scale * 918} viewBox={`0 0 ${scale * 1742} ${scale * 918}`} id="CentralPanel" >
        <image x={0} y={0} width={1742 * scale} height={918 * scale} href={center_upper_texture} />
        <circle name="us2" cx={512.5} cy={662.5} r={400} fill={"white"} fillOpacity={0.5} ></circle>
        <g name="vp">
            <circle name="" cx={2465} cy={1500} r={400} fill={"white"} fillOpacity={1.0} ></circle>
        </g>
        <rect x={2065} y={250} width={vbm_w} height={vbm_w} fillOpacity={0.8}></rect>
        <rect x={820} y={1330} width={sig_w * 4} height={sig_h * 4} fillOpacity={1.0}></rect>
        <rect x={3225} y={1500} width={sig_w * 2} height={sig_h * 3} fillOpacity={1.0}></rect>
        {/* <circle cx={2465} cy={1500} r={400} fill={"white"} fillOpacity={1.0} ></circle> */}
        <g name="rmi" transform="translate(3335,950)">
            <rect x={-rmi_w / 2} y={-rmi_h / 2 - 100} width={rmi_w} height={rmi_h} fill="#ffffffa0"></rect>
            <circle name="" cx={0} cy={0} r={370} fill="#ffffffa0" ></circle>
        </g>
    </svg >
}