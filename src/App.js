import us2 from "./us2.png"
import "./App.css"

const b = 17.8
const a = -10
const c = -170
const ticks = Array.from(Array(71)).map((_, i) => (i * 10 + 100))

// [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800]
const angles = ticks.map((t, i) => Math.sqrt(t - a) * b + c)


function US2() {
    console.log(angles)
    return <svg width={800} height={"800"} viewBox="-400 -400 800 800" unitsPerEm>
        {/* <image x={-400} y={-400} width={800} height={800} href={us2} /> */}
        <circle r={400} x={0} y={0} fillOpacity={0.5}></circle>
        <circle r={360} x={0} y={0} fill="white" fillOpacity={0.5}></circle>
        <text stroke="white" fill="white" x={-125} y={-60} fontSize={50} letterSpacing={-3} textLength={250} lengthAdjust="spacingAndGlyphs" fontFamily="lenya69">СКОРОСТЬ</text>
        {
            angles.map((a, i) => {
                const tick = ticks[i]
                if (tick % 100 === 0) {
                    return <text fontWeight={"bold"} transform={`translate(${Math.sin(a / 180 * Math.PI) * 240},${-Math.cos(a / 180 * Math.PI) * 240 + 10})`} dominantBaseline={"middle"} textAnchor="middle" stroke="white" fill="white" x={0} y={0} fontSize={100} fontFamily="lenya69">{tick / 100}</text>
                } else {
                    return null
                }

            })
        }

        {
            angles.map((a, i) => {

                const tick = ticks[i]
                if (tick % 100 === 0) {
                    return <rect x={0} y={0} width={10} height={60} transform={`translate(-5,-340) rotate(${a},5,340)`} fill="white" stroke="white"></rect>
                } else if (tick % 50 === 0) {
                    return <rect x={0} y={0} width={5} height={60} transform={`translate(-5,-340) rotate(${a},5,340)`} fill="white" stroke="white"></rect>
                } else {
                    return <rect x={0} y={0} width={5} height={30} transform={`translate(-5,-340) rotate(${a},5,340)`} fill="white" stroke="white"></rect>
                }

            })
        }

    </svg>
}

export default function App() {
    return <US2></US2>
}