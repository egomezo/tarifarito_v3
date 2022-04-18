<template>
  <div>
    <el-row style="border: 0px solid green;">
      <el-col :span="24" style="border: 0px solid blue; text-align: center;">
        <img v-if="errGif !== null" class="img-loading" :src="errGif" alt="loading...">
      </el-col>
      <el-col :span="24" style="border: 0px solid red; text-align: center;">
        <span class="text-loading"><i class="el-icon-loading" />&nbsp;Por favor espera un momento</span>
        <p>Estoy trabajando para ti</p>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import dhalsim from '@/assets/loading_images/indio.gif'
import cavernicola from '@/assets/loading_images/cavernicola.gif'
import preview from '@/assets/loading_images/preview.gif'
import statistics from '@/assets/loading_images/statistics.gif'
import wykres from '@/assets/loading_images/wykres.gif'

export default {
  name: 'PageLoading',
  data() {
    return {
      errGif: preview
    }
  },
  created() {
    this.selectImg()
  },
  methods: {
    selectImg() {
      const arrayImg = [dhalsim, cavernicola, preview, statistics, wykres]
      // const random = 0
      const random = Math.round(this.getRandomArbitrary(0, arrayImg.length - 1))
      this.errGif = arrayImg[random]
    },
    getRandomArbitrary(min, max) {
      return Math.random() * (max - min) + min
    }
  }
}
</script>

<style lang="scss" scoped>
  .img-loading {
    width: 30vw;
    height: 50vh;
  }

  .text-loading {
    color: #ff9800;
    font-size: large;
  }
</style>
