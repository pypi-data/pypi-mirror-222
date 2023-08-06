Blockly.Blocks.yolo_fast_init= {
    init: function() {
    this.appendValueInput("MODEL")
        .setCheck(String)
        .appendField("初始化FastestDet网络")
        .appendField("模型");
    this.appendValueInput("LABEL")
        .setCheck(null)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("标签");
    this.appendValueInput("WH")
        .setCheck(null)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("模型输入高宽");
    this.appendValueInput("OBJ")
        .setCheck(null)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("置信度");
    this.setInputsInline(false);
    this.setOutput(true, null);
    this.setStyle('AI_blocks');
    this.setTooltip("初始化目标检测网络");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.yolo_fast_process= {
    init: function() {
    this.appendValueInput("NAME")
        .setCheck(null)
        .appendField("运行网络");
    this.appendValueInput("IMG")
        .setCheck(null)
        .appendField("推理图片");
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setStyle('AI_blocks');
    this.setTooltip("运行FastestDet网络进行推理，返回识别结果");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.mp_face_detection= {
    init: function() {
    this.appendValueInput("VALUE")
        .setCheck(null)
        .appendField("初始化人脸检测网络")
        .appendField("阈值");
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setStyle('AI_blocks');
    this.setTooltip("初始化MediaPipe进行人脸检测");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.mp_run= {
    init: function() {
    this.appendValueInput("NAME")
        .setCheck(null)
        .appendField("运行网络");
    this.appendValueInput("IMG")
        .setCheck(null)
        .appendField("推理图片");
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setStyle('AI_blocks');
    this.setTooltip("进行推理输出结果");
    this.setHelpUrl("");
    }
  };

  
  Blockly.Blocks.mp_face_mesh= {
    init: function() {
    this.appendValueInput("MAX")
        .setCheck(null)
        .appendField("初始化面网检测网络")
        .appendField("最大识别人脸数");
    this.appendValueInput("DETE")
        .setCheck(null)
        .appendField("检测阈值");
    this.appendValueInput("TRACK")
        .setCheck(null)
        .appendField("跟踪阈值");
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setStyle('AI_blocks');
    this.setTooltip("初始化MediaPipe进行面部网格检测");
    this.setHelpUrl("https://gitcode.net/q924257/mediapipe-title/-/blob/master/face.png");
    }
  };

  Blockly.Blocks.mp_hands= {
    init: function() {
    this.appendDummyInput()
        .appendField("初始化手部检测网络");
    this.appendDummyInput()
        .appendField(" 模型复杂度")
        .appendField(new Blockly.FieldDropdown([["0","0"],["1","1"]]), "MODEL");
    this.appendValueInput("NUM")
        .setCheck(null)
        .appendField(" 手的数量");
    this.appendValueInput("DETE")
        .setCheck(null)
        .appendField(" 检测阈值");
    this.appendValueInput("TRACK")
        .setCheck(null)
        .appendField(" 跟踪阈值");
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setStyle('AI_blocks');
    this.setTooltip("初始化MediaPipe进行手部检测");
    this.setHelpUrl("https://gitcode.net/q924257/mediapipe-title/-/blob/master/hand.png");
    }
  };

  Blockly.Blocks.mp_pose= {
    init: function() {
    this.appendDummyInput()
        .appendField("初始化人体姿态检测网络");
    this.appendDummyInput()
        .appendField(" 模型复杂度")
        .appendField(new Blockly.FieldDropdown([["0","0"],["1","1"],["2","2"]]), "MODEL");
    this.appendValueInput("DETE")
        .setCheck(null)
        .appendField(" 检测阈值");
    this.appendValueInput("TRACK")
        .setCheck(null)
        .appendField(" 跟踪阈值");
    this.appendValueInput("SEG")
        .setCheck(null)
        .appendField(" 分段阈值");
    this.appendValueInput("VIS")
        .setCheck(null)
        .appendField(" 检测范围");
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setStyle('AI_blocks');
    this.setTooltip("初始化MediaPipe进行人体姿态检测");
    this.setHelpUrl("https://gitcode.net/q924257/mediapipe-title/-/blob/master/pose.png");
    }
  };

  Blockly.Blocks.audio_classify= {
    init: function() {
    this.appendValueInput("MODEL")
        .setCheck(null)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("初始化音频分类器 模型");
    this.appendValueInput("MAX")
        .setCheck(null)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("返回结果最大数量");
    this.setInputsInline(false);
    this.setOutput(true, null);
    this.setStyle('AI_blocks');
    this.setTooltip("初始化音频分类器");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.audio_classify_run= {
    init: function() {
    this.appendValueInput("VAR")
        .setCheck(null)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("运行音频分类器");
    this.appendValueInput("WAV")
        .setCheck(null)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("推理音频");
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setStyle('AI_blocks');
    this.setTooltip("运行音频分类器推理音频,结果放回一个列表对象");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.SoundThread= {
    init: function() {
    this.appendValueInput("MODEL")
        .setCheck(String)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("初始化实时音频分类器 模型");
    this.appendValueInput("MAX")
        .setCheck(Number)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("返回最大结果数量");
    this.appendValueInput("SCORE")
        .setCheck(Number)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("阈值(0~1)");
    this.setInputsInline(false);
    this.setOutput(true, null);
    this.setStyle('AI_blocks');
    this.setTooltip("初始化实时音频分类器");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.mxpit_sound_p_b_run= {
    init: function() {
    this.appendValueInput("NAME")
        .setCheck(null)
        .appendField("运行");
    this.appendDummyInput()
        .appendField("实时音频分类器,返回结果");
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setStyle('AI_blocks');
    this.setTooltip("获取实时音频分类器结果");
    this.setHelpUrl("");
    }
  };


  Blockly.Blocks.classifier_win_init= {
    init: function() {
    this.appendDummyInput()
        .appendField("初始化图像分类网络");
    this.appendValueInput("MODEL")
        .setCheck(null)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("模型");
    this.appendValueInput("CLASS")
        .setCheck(null)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("种类");
    this.setInputsInline(false);
    this.setOutput(true, null);
    this.setStyle('AI_blocks');
    this.setTooltip("初始化图像分类网络");
    this.setHelpUrl("");
    }
  };


  Blockly.Blocks.class_process= {
    init: function() {
    this.appendValueInput("NAME")
        .setCheck(null)
        .appendField("运行网络");
    this.appendValueInput("IMG")
        .setCheck(null)
        .appendField("推理图片");
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setStyle('AI_blocks');
    this.setTooltip("运行图像分类网络进行推理，返回识别结果");
    this.setHelpUrl("");
    }
  };
  

  Blockly.Blocks.mxpit_FastestDet= {
    init: function() {
    this.appendDummyInput()
        .appendField("FastestDet目标检测模型训练");
    this.appendValueInput("IMG_PATH")
        .setCheck(null)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("图片地址 ");
    this.appendValueInput("XML_PATH")
        .setCheck(null)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("标签地址 ");
    this.appendValueInput("SAVE_PATH")
        .setCheck(null)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("模型保存地址 ");
    this.appendValueInput("LABEL")
        .setCheck(null)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("标签 ");
    this.appendValueInput("BATCH_SIZE")
        .setCheck(null)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField(" Batch Size ");
    this.appendValueInput("LR")
        .setCheck(null)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("Lr(学习率)");
    this.appendValueInput("EPOCH")
        .setCheck(null)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("Epoch训练次数");
    this.setStyle('AI_blocks');
    this.setTooltip("训练目标识别模型");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.mxpit_FastestDet_p= {
    init: function() {
    this.appendValueInput("MODEL")
        .setCheck(null)
        .appendField("目标检测 加载模型(onnx)");
    this.appendValueInput("IMG")
        .setCheck(null)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("检测图像");
    this.setInputsInline(false);
    this.setOutput(true, null);
    this.setStyle('AI_blocks');
    this.setTooltip("目标识别模型预测图片");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.mxpit_cls= {
    init: function() {
    this.appendDummyInput()
        .appendField("图像分类模型训练");
    this.appendValueInput("DATA_PATH")
        .setCheck(null)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("数据集地址 ");
    this.appendValueInput("SAVE_PATH")
        .setCheck(null)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("模型保存地址 ");
    this.appendValueInput("BATCH_SIZE")
        .setCheck(null)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField(" Batch Size ");
    this.appendValueInput("LR")
        .setCheck(null)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("Lr(学习率)");
    this.appendValueInput("EPOCH")
        .setCheck(null)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("训练次数");
    this.appendValueInput("ONNX")
        .setCheck(null)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("输出onnx模型");
    this.setStyle('AI_blocks');
    this.setTooltip("目标识别模型预测图片");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.mxpit_cls_p_p= {
    init: function() {
    this.appendValueInput("MODEL")
        .setCheck(null)
        .appendField("图像分类 加载模型(pth)");
    this.appendValueInput("IMG")
        .setCheck(null)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("检测图像");
    this.setInputsInline(false);
    this.setOutput(true, null);
    this.setStyle('AI_blocks');
    this.setTooltip("图像分类模型预测图片");
    this.setHelpUrl("");
    }
  };
  
  Blockly.Blocks.mxpit_cls_p_onnx= {
    init: function() {
    this.appendValueInput("MODEL")
        .setCheck(null)
        .appendField("图像分类 加载模型(onnx)");
    this.appendValueInput("IMG")
        .setCheck(null)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("检测图像");
        this.setInputsInline(false);
        this.setOutput(true, null);
    this.setStyle('AI_blocks');
    this.setTooltip("图像分类模型预测图片");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.mxpit_sound= {
    init: function() {
    this.appendDummyInput()
        .setAlign(Blockly.ALIGN_CENTRE)
        .appendField("音频分类模型训练");
    this.appendValueInput("DATA")
        .setCheck(null)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("数据集地址");
    this.appendValueInput("SAVE")
        .setCheck(null)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("模型保存地址");
    this.appendValueInput("BATCH")
        .setCheck(null)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("Batch Size");
    this.appendValueInput("LR")
        .setCheck(null)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("Lr(学习率)");
    this.appendValueInput("EPOCH")
        .setCheck(null)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("训练次数");
    this.appendValueInput("CHUNK")
        .setCheck(null)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("音频长度");
    this.setInputsInline(false);
    this.setStyle('AI_blocks');
    this.setTooltip("训练音频分类模型");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.mxpit_sound_p= {
    init: function() {
    this.appendValueInput("MODEL")
        .setCheck(null)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("音频分类 加载模型(pt)");
    this.appendValueInput("SOUND")
        .setCheck(null)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("检测音频文件");
    this.setInputsInline(false);
    this.setOutput(true, null);
    this.setStyle('AI_blocks');
    this.setTooltip("训练音频分类模型");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.mxpit_sound_p_b= {
    init: function() {
    this.appendValueInput("MODEL")
        .setCheck(null)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("音频分类 加载模型(pt)");
    this.appendValueInput("SOUND")
        .setCheck(null)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("实时检测音频");
    this.appendValueInput("TIME")
        .setCheck(null)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("录音时长");
    this.setInputsInline(false);
    this.setOutput(true, null);
    this.setStyle('AI_blocks');
    this.setTooltip("预测音频分类模型");
    this.setHelpUrl("");
    }
  };


  Blockly.Blocks.mxpit_sound_p_b= {
    init: function() {
    this.appendDummyInput()
        .appendField("初始化音频分类网络");
    this.appendValueInput("MODEL")
        .setCheck(null)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("加载模型(pt)");
    this.appendValueInput("TIME")
        .setCheck(null)
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("录音时长");
    this.setInputsInline(false);
    this.setOutput(true, null);
    this.setStyle('AI_blocks');
    this.setTooltip("初始化音频分类模型实时识别网络");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.cnocr_init= {
    init: function() {
    this.appendDummyInput()
        .appendField("初始化OCR识别");
    this.appendDummyInput()
        .appendField("模式")
        .appendField(new Blockly.FieldDropdown([["默认识别","none"],["快速识别","fast"],["竖排文字识别","shupai"],["英文识别","en"],["繁体中文识别","chinese_cht"]]), "MODE");
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setStyle('AI_blocks');
    this.setTooltip("初始化OCR实例");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.cnocr_ocrimg= {
    init: function() {
    this.appendValueInput("NAME")
        .setCheck(null);
    this.appendValueInput("IMG")
        .setCheck(null)
        .appendField("识别图像对象");
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setStyle('AI_blocks');
    this.setTooltip("OCR实例识别图像");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.cnocr_ocrfile= {
    init: function() {
    this.appendValueInput("NAME")
        .setCheck(null);
    this.appendValueInput("IMG")
        .setCheck(null)
        .appendField("识别图像文件");
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setStyle('AI_blocks');
    this.setTooltip("OCR实例识别图像文件");
    this.setHelpUrl("");
    }
  };