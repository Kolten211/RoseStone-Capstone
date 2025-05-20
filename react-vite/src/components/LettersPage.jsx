import { useRef } from "react"

function SoundLetter({ letter, soundFile }) {
    const audioRef = useRef(null);

    const handleClick = (e) => {
        e.preventDefault();
        audioRef.current.play();
    };
    

    return (
        <span>
            <a onClick={handleClick}>{letter}</a>
            <audio ref={audioRef} src={soundFile}></audio>
        </span>
    )
}

function LettersPage(){


    return (
        <div>
            <h1 className="title">The Alphabet</h1>
            <div>
                <div>
                    <SoundLetter letter="A" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Letter+A.wav" />
                    <SoundLetter letter="a" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Sound+A.wav"/>
                </div>
                <div>
                    <SoundLetter letter="B" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Letter+B.wav" />
                    <SoundLetter letter="b" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Sound+B.wav" />
                </div>
                <div>
                    <SoundLetter letter="C" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Letter+C.wav" />
                    <SoundLetter letter="c" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Sound+C.wav" />
                </div>
                <div>
                    <SoundLetter letter="D" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Letter+D.wav" />
                    <SoundLetter letter="d" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Sound+D.wav" />
                </div>
                <div>
                    <SoundLetter letter="E" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Letter+E.wav" />
                    <SoundLetter letter="e" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Sound+E.wav" />
                </div>
                <div>
                    <SoundLetter letter="F" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Letter+F.wav" />
                    <SoundLetter letter="f" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Sound+F.wav" />
                </div>
                <div>
                    <SoundLetter letter="G" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Letter+G.wav" />
                    <SoundLetter letter="g" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Sound+G.wav" />
                </div>
                <div>
                    <SoundLetter letter="H" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Letter+H.wav" />
                    <SoundLetter letter="h" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Sound+H.wav" />
                </div>
                <div>
                    <SoundLetter letter="I" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Letter+I.wav" />
                    <SoundLetter letter="i" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Sound+I.wav" />
                </div>
                <div>
                    <SoundLetter letter="J" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Letter+J.wav" />
                    <SoundLetter letter="j" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Sound+J.wav" />
                </div>
                <div>
                    <SoundLetter letter="K" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Letter+K.wav " />
                    <SoundLetter letter="k" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Sound+K.wav" />
                </div>
                <div>
                    <SoundLetter letter="L" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Letter+L.wav" />
                    <SoundLetter letter="l" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Sound+L.wav" />
                </div>
                <div>
                    <SoundLetter letter="M" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Letter+M.wav" />
                    <SoundLetter letter="m" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Sound+M.wav" />
                </div>
                <div>
                    <SoundLetter letter="N" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Letter+N.wav" />
                    <SoundLetter letter="n" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Sound+N.wav" />
                </div>
                <div>
                    <SoundLetter letter="O" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Letter+O.wav" />
                    <SoundLetter letter="o" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Sound+O.wav" />
                </div>
                <div>
                    <SoundLetter letter="P" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Letter+P.wav" />
                    <SoundLetter letter="p" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Sound+P.wav" />
                </div>
                <div>
                    <SoundLetter letter="Q" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Letter+Q.wav" />
                    <SoundLetter letter="q" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Sound+Q.wav" />
                </div>
                <div>
                    <SoundLetter letter="R" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Letter+R.wav" />
                    <SoundLetter letter="r" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Sound+R.wav" />
                </div>
                <div>
                    <SoundLetter letter="S" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Letter+S.wav" />
                    <SoundLetter letter="s" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Sound+S.wav" />
                </div>
                <div>
                    <SoundLetter letter="T" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Letter+T.wav" />
                    <SoundLetter letter="t" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Sound+T.wav" />
                </div>
                <div>
                    <SoundLetter letter="U" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Letter+U.wav" />
                    <SoundLetter letter="u" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Sound+U.wav" />
                </div>
                <div>
                    <SoundLetter letter="V" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Letter+V.wav" />
                    <SoundLetter letter="v" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Sound+V.wav" />
                </div>
                <div>
                    <SoundLetter letter="W" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Letter+W.wav" />
                    <SoundLetter letter="w" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Sound+W.wav" />
                </div>
                <div>
                    <SoundLetter letter="X" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Letter+X.wav" />
                    <SoundLetter letter="x" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Sound+X.wav" />
                </div>
                <div>
                    <SoundLetter letter="Y" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Letter+Y.wav" />
                    <SoundLetter letter="y" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Sound+Y.wav" />
                </div>
                <div>
                    <SoundLetter letter="Z" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Letter+Z.wav" />
                    <SoundLetter letter="z" soundFile="https://rosestonebucket.s3.us-east-1.amazonaws.com/Sound+Z.wav" />
                </div>
            </div>
        </div>
    )
}

export default LettersPage