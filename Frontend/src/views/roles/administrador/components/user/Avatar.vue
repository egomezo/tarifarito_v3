<template>
  <div>
    <el-row style="text-align: center;">
      <el-col :xs="24" :md="24" style="border: 0px solid red;">
        <pan-thumb :image="image" class="panThumb" />
      </el-col>
      <el-col :xs="24" :md="24" style="border: 0px solid red; height: 4vh; padding-top: 0.5%;">
        <span style="font-size: small; color: gray; cursor: pointer;" @click="imagecropperShow = true">Cambiar foto</span>
      </el-col>
    </el-row>

    <image-cropper
      v-show="imagecropperShow"
      :key="imagecropperKey"
      :width="300"
      :height="300"
      lang-type="es-MX"
      @close="close"
      @crop-success="cropSuccess"
    />
  </div>
</template>

<script>
import ImageCropper from '@/components/ImageCropper'
import PanThumb from '@/components/PanThumb'
import { DATA } from '@/data/ImgUser'
export default {
  name: 'AvatarUpload',
  components: { ImageCropper, PanThumb },
  props: {
    img: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      imagecropperShow: false,
      imagecropperKey: 0,
      image: this.img
    }
  },
  watch: {
    img: {
      deep: true,
      async handler(val) {
        if (val) {
          this.image = val
        } else {
          this.image = DATA.imageURL
        }
        // console.log('Imagen -> ', this.image)
      }
    }
  },
  methods: {
    /**
     * crop success
     *
     * [param] imgDataUrl
     * [param] field
     */
    cropSuccess(imgDataUrl, field) {
      // console.log('-------- crop success --------')
      this.imagecropperKey = this.imagecropperKey + 1 // Comentar linea si desea subir la imagen
      this.imagecropperShow = false // Comentar linea si desea subir la imagen al servidor
      this.image = imgDataUrl
      this.$emit('preview-files', this.image)
    },
    /**
     * upload success
     *
     * [param] jsonData  server api return data, already json encode
     * [param] field
     */
    cropUploadSuccess(jsonData, field) {
      // console.log('-------- upload success --------')
      console.log(jsonData)
      console.log('field: ' + field)
    },
    /**
     * upload fail
     *
     * [param] status    server api return error status, like 500
     * [param] field
     */
    cropUploadFail(status, field) {
      // console.log('-------- upload fail --------')
      console.log(status)
      console.log('field: ' + field)
    },
    close() {
      this.imagecropperShow = false
    }
  }
}
</script>

<style scoped>
.panThumb {
  z-index: 100;
  height: 130px!important;
  width: 130px!important;
}
</style>
