# Files needed by [TensorFlow Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection)

1. The file "create_duckie_tf_record.py" will transform your raw images and ".xml" format labels (bounding boxes) into 
TFRecord format, which will be used as input for training. [Check here](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/preparing_inputs.md)
2. The file "duckie_label_map.pbtxt" will be used for training and inference.