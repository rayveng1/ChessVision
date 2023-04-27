import "./Main.css";
import Roboflow from "../components/roboflow.js";

export default function Main() {
	return (
	  <main className="max-w-2xl mx-auto">
		ChessVision - Rayven/Connor/Piyush/Thejas
		<div className="w-full h-full">
		  <Roboflow modelName="piece-detection-rayven" modelVersion="4" />
		</div>
	  </main>
	)
  }