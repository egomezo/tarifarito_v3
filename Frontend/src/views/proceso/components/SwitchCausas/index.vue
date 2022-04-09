<template>
  <el-col :md="24" style="border: 0px solid blue;">
    <el-card>
      <div slot="header" class="clearfix">
        <el-row>
          <el-col :md="countCausales > 0 ? 22 : 22">
            <span>{{ title }}</span>
          </el-col>
          <el-col :md="countCausales > 0 ? 0 : 2">
            <el-switch v-show="countCausales > 0 ? false : true" v-model="valSwitch" active-color="#13ce66" />
          </el-col>
          <el-col v-show="countCausales > 0" :md="countCausales > 0 ? 2 : 0">
            <div class="badge-tercero">
              <el-badge :value="countCausales" class="item" type="success">
                <el-link icon="el-icon-message-solid" :underline="false" @click="dialogDrawer = true" />
              </el-badge>
            </div>
          </el-col>
        </el-row>
      </div>

      <el-row>
        <el-col v-loading="loading" :span="24">
          <el-card shadow="never" style="border: 1px solid #F2F6FC; height: 18em; overflow-y: scroll;" class="card-causas">
            <div v-if="countCausales === 0" style="border: 0px solid; height: 15em; text-align: center; display: flex; align-items: center; padding-left: 28%;">
              <span style="color: #C0C4CC; font-size: small;"><b>Proceso no registra causas</b></span>
            </div>
            <transition name="el-fade-in-linear">
              <div v-show="countCausales" class="card-causa">
                <el-card v-for="item in cantidadCausasProceso" :key="item.idcausal" shadow="never" style="height: 5vh; margin-bottom: 2%;">
                  <el-row>
                    <el-col :span="22">
                      <span style="color: #606266; font-size: small;">■ {{ item.nombrecausal }}</span>
                    </el-col>
                    <el-col :span="2">
                      <span style="color: #d9534f; font-size: medium; ">{{ item.cantidad }}</span>
                    </el-col>
                  </el-row>
                </el-card>
              </div>
            </transition>
          </el-card>
        </el-col>
      </el-row>
    </el-card>

    <!-- Cuadro de dialogo para agregar causal -->

    <ModalAgregar
      :modaltitulo="tituloModalItem"
      :modalvisible="dialogVisible"
      :modalform="formItem"
      :domcomponents="domItem"
      :rulesform="rulesFormItem"
      :datamodal="dataFormItem"
      :action="modalAction"
      @confirmar="handleConfirmar"
    />

    <ListaCausales
      drawertitulo="Causales"
      :dialogdrawer="dialogDrawer"
      :datacausal="causas"
      :editar="editar"
      :idproceso="idproceso"
      @updateView="handleUpdateView"
      @closedrawer="handleClose"
    />
  </el-col>
</template>

<script>
import ModalAgregar from '@/components/ModalAgregar'
import { CONSTANTS } from './constants/constants'
import ListaCausales from './ListaCausales'
import { getCausalProceso, getCantidadCausalProceso, createCausal } from '@/api/procesosDIEG/causal'

export default {
  directives: { },
  components: { ModalAgregar, ListaCausales },
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
      loading: false,
      abogadoEditar: this.editar,
      valSwitch: false,
      switchDisable: false,
      countCausales: 0,
      dialogVisible: false,
      tituloModalItem: '',
      formItem: CONSTANTS.formItem,
      domItem: CONSTANTS.domItem,
      rulesFormItem: CONSTANTS.rulesFormItem,
      dataFormItem: CONSTANTS.dataFormItem,
      modalAction: '',
      dialogDrawer: false,
      causas: [],
      cantidadCausasProceso: []
    }
  },
  watch: {
    valSwitch: {
      deep: true,
      handler(val) {
        // console.log('valSwitch - > ', val)
        if (this.countCausales > 0) {
          this.valSwitch = true
          this.switchDisable = true
        } else {
          this.switchDisable = false
          this.valSwitch = false
          if (!this.dialogDrawer) {
            this.dialogVisible = true
            this.modalAction = 'Agregar'
            this.tituloModalItem = 'Agregar causal'
          }
        }
      }
    }
  },
  mounted() {
    this.initView()
  },
  methods: {
    async initView() {
      this.getCausales()
      this.getCantidadCausal()
    },
    handleUpdateView() {
      this.getCausales()
      this.getCantidadCausal()
    },
    async getCausales() { // Actualiza la lista de causas luego de agregar / editar
      await getCausalProceso(this.idproceso).then((response) => {
        // console.log('CAUSALES -> ', response) // Cantidad de causales
        this.countCausales = response.length
        if (response.length) {
          this.causas = response
        } else {
          this.dialogDrawer = false
        }
      })
    },
    async getCantidadCausal() {
      await getCantidadCausalProceso(this.idproceso).then((response) => {
        // console.log('CANTIDAD CAUSALES PROCESO -> ', response)
        this.cantidadCausasProceso = response
      })
    },
    handleClose(resp) {
      // console.log('cerrar drawer ->> ', resp)
      this.dialogDrawer = resp
      // this.$destroy()
    },
    async handleConfirmar(modal) { // Funcion que captura los eventos que devuelve el modal de [editar / agregar] causal
      // console.log(modal)
      if (modal.action === 'Agregar') {
        // console.log(modal)
        modal.data.idproceso = parseInt(this.idproceso)
        if (!modal.data.hasOwnProperty('descripcion')) {
          modal.data.descripcion = ''
        }
        await createCausal(modal.data).then(async(response) => {
          this.$notify({
            title: 'Buen trabajo!',
            message: 'Causal agregada con éxito',
            position: 'bottom-right',
            type: 'success',
            duration: 2000
          })
          this.handleUpdateView()
        }, (err) => {
          console.log(err)
          this.$notify({
            title: 'Advertencia',
            message: 'No se pudo completar la operación!',
            position: 'bottom-right',
            type: 'warning',
            duration: 2000
          })
        })
        this.handleUpdateView()
      }
      this.dialogVisible = false
      this.formItem = {} // Se reinicia el modelo del modal (importante)
    }
  }
}
</script>

<style lang="scss" scoped>
  /* width */
  ::-webkit-scrollbar {
    width: 1px;
  }

  /* Track */
  ::-webkit-scrollbar-track {
    background: #f1f1f1;
  }

  /* Handle */
  ::-webkit-scrollbar-thumb {
    background: #888;
  }

  /* Handle on hover */
  ::-webkit-scrollbar-thumb:hover {
    background: #555;
  }
</style>

<style>
  .card-causas .el-card__body {
    border: 0px solid;
    padding-top: 4%;
  }

  .card-causa .el-card__body {
    border: 0px solid;
    padding-top: 2%;
  }
</style>
