# Yuru-Flat Lora

The Yuru-Flat Lora is distributed under the [Fair AI Public License 1.0-SD](https://freedevproject.org/faipl-1.0-sd/). In compliance with the license requirements, the following documentation details the steps involved in the creation of this Lora.

## Creation Process

1. **Initial Image**: Start with the `Original.png` file available in this repository.

2. **Image Transformation**:
   - Use the `img2img` to convert `Original.png` to `Temp.png`.
   - Perform another `img2img` to transform `Temp.png` into `Target.png`.
   - The parameters used in the `img2img` processes are included in the metadata of the respective PNG files in this repository.

3. **Model Training**:
   - Utilize the [sd-webui-traintain](https://github.com/hako-mikan/sd-webui-traintrain) plugin.
   - Set the plugin to `Difference` mode using the `Difference_Use2ndPass` preset.
   - Specify `Original.png` as the `Original` and `Target.png` as the `Target`.
   - The output from this step will be `test_yurucamp.safetensors`.

4. **Lora Pruning**:
   - Run the `loraedit.py` script to prune the Lora.
   - The final output, `yuru_flat.safetensors`, is the pruned Lora ready for use.