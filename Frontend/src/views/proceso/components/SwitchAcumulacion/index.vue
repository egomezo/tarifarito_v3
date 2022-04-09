<template>
  <el-col :md="24" style="border: 0px solid blue; padding-top: 10px;">
    <el-card>
      <el-row>
        <el-col :md="countNotificaciones > 0 ? 22 : 22">
          <span>{{ title }}</span>
        </el-col>
        <el-col :md="countNotificaciones > 0 ? 0 : 2">
          <el-switch v-show="countNotificaciones > 0 ? false : true" v-model="valSwitch" active-color="#13ce66" :disabled="switchDisable || !abogadoEditar" />
        </el-col>
      </el-row>
    </el-card>
  </el-col>
</template>

<script>
export default {
  directives: { },
  components: { },
  props: {
    idproceso: {
      type: String,
      required: true
    },
    editar: {
      type: Boolean,
      required: true
    },
    title: {
      type: String,
      default: ''
    }
  },
  data() {
    return {
      abogadoEditar: this.editar,
      valSwitch: false,
      switchDisable: true,
      countNotificaciones: 0
    }
  },
  mounted() {
  },
  methods: {
  }
}
</script>
