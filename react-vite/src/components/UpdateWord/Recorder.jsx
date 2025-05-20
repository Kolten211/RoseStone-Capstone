import { useState, useRef} from 'react';
// import Recorder from 'recorder-js';


function VoiceRecorder({ onAudioRecorded }) {
    const [isRecording, setIsRecording] = useState(false);
    // const [isPaused, setIsPaused] = useState(false);
    const [audioURL, setAudioURL] = useState(null);
    const mediaRecorder = useRef(null);
    const audioChunks = useRef([]);
    const stream = useRef(null);
    // const gumStream = useRef(null);
    // const rec = useRef(null);
    // const input = useRef(null);
    // const audioContext = useRef(null);


    // useEffect(() => {
    //     const AudioContext = window.AudioContext || window.webkitAudioContext
    //     audioContext.current = new AudioContext()
    //     console.log(audioContext.current)
    // }, []);

    const startRecording = async (event) => {
        event.preventDefault()
        try {
            stream.current = await navigator.mediaDevices.getUserMedia({ audio: true});
            mediaRecorder.current = new MediaRecorder(stream.current);

            mediaRecorder.current.ondataavailable = (event) => {
                audioChunks.current.push(event.data)
            };

            mediaRecorder.current.onstop = () => {
                const audioBlob = new Blob(audioChunks.current, { type: 'audio/wav' });
                const url = URL.createObjectURL(audioBlob)
                setAudioURL(url);
                audioChunks.current = [];
                onAudioRecorded(audioBlob);
            }

            mediaRecorder.current.start();
            setIsRecording(true);
        } catch (error) {
            console.error('Error accessing microphone', error);
        }
        // console.log("start recording clicked")
        // try {
        //     const contraints = {
        //         audio: true,
        //         video: false
        //     };
            // gumStream.current = await navigator.mediaDevices.getUserMedia(contraints);
            // if (audioContext.current.state === 'suspeneded') {
            //     await audioContext.current.resume()
            // }
            // input.current = audioContext.current.createMediaStreamSource(gumStream.current);
            // console.log("gumStream.current:", gumStream.current);
            // console.log("input.current:", input.current);
            // console.log("Contructor", Recorder)
            // console.log("Context", audioContext.current)
        //     rec.current = new Recorder(audioContext.current, {numChannels: 1 });
        //     console.log('rec.current', rec.current)
        //     rec.current.record();
        //     setIsRecording(true);
        //     setIsPaused(false)
        // } catch (error) {
        //     console.error('Error accessing microphone', error)
        // }
    }

    const stopRecording = (event) => {
        event.preventDefault()
        if (mediaRecorder.current && mediaRecorder.current.state === 'recording') {
            mediaRecorder.current.stop();
            setIsRecording(false);
            if (stream.current) {
                stream.current.getTracks().forEach((track) => track.stop())
            }
        }
        // if (rec.current) {
        //     rec.current.stop();
        //     gumStream.current.getAudioTracks()[0].stop();
        //     rec.current.exportWAV((blob) => {
        //         const url = URL.createObjectURL(blob);
        //         setAudioURL(url)
        //     })
        //     setIsRecording(false);
        //     setIsPaused(false);
        // }
    }

    // const pauseRecording = () => {
    //     if (rec.current) {
    //         if (isRecording && !isPaused) {
    //             rec.current.stop();
    //             setIsPaused(true)
    //         } else if (isRecording && isPaused) {
    //             rec.current.record();
    //             setIsPaused(false);
    //         }
    //     }
    // }

    return (
        <div>
            <button type="button" onClick={startRecording} disabled={isRecording}>
                Start
            </button>
            <button type="button" onClick={stopRecording} disabled={!isRecording}>
                Stop
            </button>
            {/* <button onClick={pauseRecording} disabled={!isRecording}>
                {isPaused ? 'Resume' : 'Pause'}
            </button> */}
            {audioURL && <audio src={audioURL} controls />}
        </div>
    )
}

export default VoiceRecorder