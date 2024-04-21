from safetensors import safe_open
from datetime import datetime
from safetensors.torch import save_file

MODEL_NAME = "test_yurucamp"
OUTPUT_NAME = "yuru_flat"

INPUT_FILE = f"{MODEL_NAME}.safetensors"
OUTPUT_FILE = f"{OUTPUT_NAME}.safetensors"
BLOCKS_TO_SAVE = [
    #"lora_unet_middle_block_1", 
    #"lora_unet_output_blocks_0", 
    #"lora_unet_output_blocks_1",
    #"lora_unet_input_blocks_8",
    #"lora_unet_input_blocks_7"，
    #"lora_unet_output",
    "lora_unet_up",
    ]

tensors = {}
with safe_open(INPUT_FILE, framework="pt") as f:
    metadata = f.metadata()
    # remove lora hash
    if 'sshs_legacy_hash' in metadata:
        del metadata['sshs_legacy_hash']
    if 'sshs_model_hash' in metadata:
        del metadata['sshs_model_hash']
    if 'ss_output_name' in metadata:
        del metadata['ss_output_name']

    metadata['modelspec.date'] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

    for k in f.keys():
        # if any of BLOCKS_TO_SAVE is the prefix of k
        if any(k.startswith(b) for b in BLOCKS_TO_SAVE):
            tensors[k] = f.get_tensor(k)

save_file(tensors, OUTPUT_FILE, metadata)

