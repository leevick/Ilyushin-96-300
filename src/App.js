import us2 from "./us2.png"

function US2() {
    return <svg width={800} height={"800"} viewBox="-400 -400 800 800" unitsPerEm>
        <image x={-400} y={-400} width={800} height={800} href={us2} />
        <line transform="rotate(1,0,0)" x1={0} y1={0} x2={0} y2={-400} stroke="white" strokeWidth={2}></line>
        <circle r={400} x={0} y={0} fillOpacity={0.5}></circle>
        <circle r={360} x={0} y={0} fill="white" fillOpacity={0.5}></circle>
        <text x={-100} y={-60} fontSize={40} textLength={250} lengthAdjust="spacingAndGlyphs" fontFamily="Sarasa Mono SC">СКОРОСТЬ</text>
    </svg>
}

export default function App() {
    return <US2></US2>
}