#coding=utf-8
from copy import deepcopy
from math import ceil, sqrt
from .wires import crt_Wires
from physicsLab._tools import numType
from typing import Union as Union, List, Tuple
from physicsLab.element import get_Element
import physicsLab.electricity.elementXYZ as _elementXYZ
import physicsLab.electricity.elementsClass as _elementsClass
from physicsLab.electricity.unionElements.unionLogic import D_WaterLamp
import physicsLab.electricity.unionElements._unionClassHead as _unionClassHead

noteType = List[Union[None, "Note"]] # 音符类型
chordType = Union[Tuple["Note"], List["Note"]] # 和弦类型

# midi类，用于提供physicsLab与midi文件之间的桥梁
class Midi:
    def __init__(self) -> None:
        pass

    # 播放midi类存储的信息
    def sound(self):
        pass

    # 转换为physicsLab的piece类
    def translate_to_piece(self) -> "Piece":
        pass

# 音符类
class Note:
    def __init__(self,
                 time: int, # 在音轨中播放的时间
                 playTime: int = 1,  # 音符发出声音的时长 暂时不支持相关机制
                 instrument: Union[int, str] = 0, # 演奏的乐器，暂时只支持传入数字
                 pitch: Union[int, str] = 60, # 音高/音调
                 volume: numType = 1.0 # 音量/响度
    ) -> None:
        if not (
                isinstance(time, int) or
                isinstance(playTime, int) or
                isinstance(instrument, (int, str)) or
                isinstance(pitch, (int, str)) or
                isinstance(volume, float)
        ):
            raise TypeError
        self.instrument = instrument
        self.pitch = pitch
        self.volume = volume
        self.time = time
        self.playTime = playTime

    def __str__(self) -> str:
        return f"<union.Note Object=> time:{self.time}, playTime:{self.playTime}, instrument: {self.instrument}, " \
               f"pitch: {self.pitch}, volume: {self.volume}>"

# 循环类，用于创建一段循环的音乐片段
class Loop:
    def __init__(self, notes: Union[chordType, "Loop"], loopTime: int = 2) -> None:
        if not(
            isinstance(notes, (Loop, tuple, list)) or
            isinstance(loopTime, int)
        ) or any(not isinstance(a_note, Note) for a_note in notes) or loopTime < 2:
            raise TypeError

        if isinstance(notes, Loop):
            raise RuntimeError("Sorry, this is not supported for the moment")

        self.notes = tuple(*notes)
        self.loopTime = loopTime
        self.cases = []

    # loop-case: 每次主循环执行完一遍后会依次播放case中的音符
    def case(self, *notes) -> "Loop":
        self.cases.append(deepcopy(notes))
        return self

# 音轨
class Track:
    def __init__(self,
                 notes: Union[List[Union[Note, Loop]], Tuple[Union[Note, Loop]]],
                 # 设置整个音轨的默认参数 Track global variable
                 instrument: int = 0, # 演奏的乐器，暂时只支持传入数字
                 pitch: int = 60, # 音高/音调
                 bpm: int = 100, # 节奏
                 volume: float = 1.0 # 音量/响度
    ) -> None:
        if not (
                isinstance(instrument, int) or
                isinstance(pitch, int) or
                isinstance(bpm, int) or
                0 < volume < 1 or
                isinstance(notes, (list, tuple, Loop)) and all(isinstance(val, Note) for val in notes)
        ):
            raise TypeError

        self.instrument = instrument
        self.pitch = pitch
        self.bpm = bpm
        self.volume = volume
        self.notes: noteType = []
        for a_note in notes:
            tick = 1
            while tick < a_note.time:
                tick += 1
                self.notes.append(None)
            self.notes.append(deepcopy(a_note))

    def __len__(self) -> int:
        return len(self.notes)

    def __str__(self):
        return f"Track: {self.notes}"
    # iterator
    def __iter__(self):
        self.__iter = iter(self.notes)
        return self.__iter

    def __next__(self):
        for a_note in self.__iter:
            yield a_note

# 乐曲类
class Piece:
    def __init__(self, *tracks: Track):
        if not all(isinstance(a_track, Track) for a_track in tracks):
            raise TypeError

        self.tracks: Track = tracks
        self.mergeTrack()

    def __len__(self):
        return len(self.notes)

    def __getitem__(self, item):
        return self.notes[item]

    # iterator
    def __iter__(self):
        self.__iter = iter(self.notes)
        return self.__iter

    def __next__(self):
        for a_note in self.__iter:
            yield a_note
    
    # 将多个音轨合并为一个音轨（方便物实生成）
    def mergeTrack(self) -> "Piece":
        if len(self.tracks) > 1:
            raise RuntimeError("Sorry, multiple tracks are not supported for the moment")
        
        self.notes = self.tracks[0].notes
        
        return self

    # 在物实生成对应的电路
    def play(self, x:numType = 0, y: numType = 0, z: numType = 0, elementXYZ = None) -> None:
        Player(self, x, y, z, elementXYZ)

    # 转换为Midi类
    def translate_to_midi(self) -> Midi:
        pass

# 将piece的数据生成为物实的电路
class Player(_unionClassHead.UnionBase):
    def __init__(self,
                 musicArray: Union[Piece, List[Piece], Tuple[Piece]],
                 x: numType = 0, y: numType = 0, z: numType = 0,
                 elementXYZ = None
    ):
        if not (
                isinstance(x, (int, float)) or
                isinstance(y, (int, float)) or
                isinstance(z, (int, float))
        ) or not(
                isinstance(musicArray, Piece) or
                all(isinstance(a_piece, Piece) for a_piece in musicArray)
        ):
            raise TypeError

        if not (elementXYZ == True or (_elementXYZ.is_elementXYZ() == True and elementXYZ is None)):
            x, y, z = _elementXYZ.translateXYZ(x, y, z)

        if isinstance(musicArray, (tuple, list)):
            if len(musicArray) > 1:
                raise RuntimeError("Sorry, multiple pieces are not supported for the moment")
            musicArray: Piece = musicArray[0]

        # 计算音乐矩阵的长宽
        side = None
        if len(musicArray) >= 2:
            side = ceil(sqrt(len(musicArray)))
        else:
            side = 2

        tick = _elementsClass.Nimp_Gate(x + 1, y, z, True)
        counter = _elementsClass.Counter(x, y + 1, z, True)
        _elementsClass.Logic_Input(x, y, z, True).o - tick.i_up
        tick.o - tick.i_low
        tick.o - counter.i_up

        xPlayer = D_WaterLamp(x + 1, y + 1, z, unionHeading=True, bitLength=side, elementXYZ=True)
        yPlayer = D_WaterLamp(x, y + 3, z, bitLength=side, elementXYZ=True, is_loop=False).set_HighLeaveValue(1.5)

        yesGate = _elementsClass.Yes_Gate(x + 1, y + 2, z + 1, True)
        xPlayer[0].o_low - yesGate.i
        crt_Wires(counter.o_upmid, xPlayer.data_Input)
        crt_Wires(xPlayer.data_Output[0], yPlayer.data_Input)

        # main
        xcor, ycor, zcor = 0, 0, 0
        for a_note_item, a_note in enumerate(musicArray):
            if a_note is not None:
                # 当time==0时，则为和弦（几个音同时播放）
                # 此时生成的简单乐器与z轴平行
                if zcor != 0:
                    ins = _elementsClass.Simple_Instrument(
                        1 + x + xcor, 4 + y + ycor, z + zcor, pitch=a_note.pitch, elementXYZ=True
                    )
                    ins.i - get_Element(x=1 + x + xcor, y=4 + y + ycor, z=z + zcor - 1).i
                    ins.o - get_Element(x=1 + x + xcor, y=4 + y + ycor, z=z + zcor - 1).o
                else:
                    ins = _elementsClass.Simple_Instrument(
                        1 + x + xcor, 4 + y + ycor, z, pitch=a_note.pitch, elementXYZ=True
                    )
                    # 连接x轴的d触的导线
                    if xcor == 0:
                        yesGate.o - ins.o
                    else:
                        ins.o - xPlayer.data_Output[xcor]
                    # 连接y轴的d触的导线
                    ins.i - yPlayer.neg_data_Output[ycor // 2]

                i = 1
                exit_sign = None
                while True:
                    if a_note_item + i >= len(musicArray):
                        exit_sign = True
                        break
                    if musicArray[a_note_item+i] is None:
                        i += 1
                    else:
                        break
                if exit_sign:
                    break
                next_note = musicArray[a_note_item+i]
                if a_note_item+1 < len(musicArray) and next_note is not None and next_note.time != 0:
                    zcor = 0
                else:
                    zcor += 1
                    continue

            xcor += 1
            if xcor == side:
                xcor = 0
                ycor += 2
