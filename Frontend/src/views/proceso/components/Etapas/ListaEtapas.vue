<template>
  <div v-loading="loadingEtapas" class="main-article" style="background: #f7fbff; padding-left: 50px;">
    <el-row :gutter="30" class="header-agregar-etapa">
      <el-col v-for="(etapa, index) in etapas" :key="etapa.idtetapa" :sm="24" :md="8" style="border: 0px solid red; padding: 15px;">
        <el-card class="card-etapa" style="border: 0px solid #DCDFE6;">
          <div slot="header" class="clearfix" style="border: 0px solid red; padding: 0;">
            <div style="border-radius: 3px;padding-top: 2%;padding-right: 4%;height: 8vh;background: linear-gradient(38deg, rgba(255,255,255,1) 84%, rgba(33,133,208,1) 85%, rgba(33,133,208,1) 86%);">
              <el-row>
                <el-col :span="24" style="border: 0px solid red; text-align: right; color: white;">
                  <b>{{ index + 1 }}</b>
                </el-col>
                <el-col :span="24" style="border: 0px solid red; text-align: center; color: #2184d0;">
                  <b>{{ etapa.nombre }}</b><br>
                  <b v-if="etapa.varios_actos === 'SI'">[{{ etapa.nombre_acto }}]</b>
                </el-col>
              </el-row>
            </div>
          </div>
          <!-- Contenido de la card cuando la etapa NO tiene varios actos -->
          <el-row class="div-acto">
            <el-col :span="24" style="border: 0px solid; padding: 5% 10%;">
              <div class="text item" style="padding-top: 3%;">
                <el-row>
                  <el-col :span="12" :xs="7">
                    <span style="color: #606266;"><b>Radicado</b></span>
                  </el-col>
                  <el-col :span="12" :xs="17">
                    <span style="color: #606266;">{{ etapa.radicado }}</span>
                  </el-col>
                </el-row>
                <el-divider />
              </div>
              <div class="text item">
                <el-row>
                  <el-col :span="12" :xs="7">
                    <span style="color: #606266;"><b>Fecha radicado</b></span>
                  </el-col>
                  <el-col :span="12" :xs="17">
                    <span v-if="etapa.fechaInicio !== null" style="color: #606266;"><i class="el-icon-time" /> {{ etapa.fechaInicio | formatDate }}</span>
                    <span v-else style="color: #606266;">No registra</span>
                  </el-col>

                  <el-col v-if="etapa.fecha_recepcion === 'SI'" :span="12" :xs="7" style="padding-top: 10px;">
                    <span style="color: #606266;"><b>Fecha Recepción</b></span>
                  </el-col>
                  <el-col v-if="etapa.fecha_recepcion === 'SI'" :span="12" :xs="17" style="padding-top: 10px;">
                    <span v-if="etapa.fechaRecepcion !== null" style="color: #606266;"><i class="el-icon-time" /> {{ etapa.fechaRecepcion | formatDate }}</span>
                    <span v-else style="color: #606266;">No registra</span>
                  </el-col>
                </el-row>
              </div>
              <el-divider />
              <div v-if="etapa.campo_observacion === 'SI'" class="text item">
                <!-- <span style="color: #606266;"><b>Observación</b></span><br><br> -->
                <el-button v-if="etapa.observacion" type="text" @click="openDialogObservacion(etapa.observacion)">Click para ver la observación</el-button>
                <!-- <el-input
                  v-model="etapa.observacion"
                  type="textarea"
                  class="control-modal"
                  rows="8"
                  readonly
                /> -->
              </div>
            </el-col>
            <el-col :span="24" class="bottom">
              <el-button
                :disabled="!editar"
                style="border: 1px solid #67C23A"
                size="mini"
                type="success"
                plain
                icon="el-icon-edit"
                @click="handleEditarEtapa(etapa)"
              ><b>Editar</b></el-button>
              <el-button
                v-show="etapa.etapa !== 1 || !editar"
                size="mini"
                type="danger"
                plain
                icon="el-icon-delete"
                @click="handleBorrarEtapa(etapa)"
              />
            </el-col>
          </el-row>
        </el-card>
      </el-col>
    </el-row>

    <!-- Cuadro de dialogo para editar etapa -->

    <ModalAgregar
      :modaltitulo="tituloModalItem"
      :modalvisible="dialogVisibleItem"
      :modalform="formItem"
      :domcomponents="domItem"
      :rulesform="rulesFormItem"
      :datamodal="dataFormItem"
      :action="modalAction"
      @confirmar="handleConfirmar"
    />

    <!-- Modal de confirmacion para borrar una etapa -->

    <ModalDelete
      titulo="Advertencia"
      :mensaje="mensajeModalDelete"
      :modalvisible="deleteDialogVisible"
      @confirmar="submitDelete"
    />

    <!-- Modal para mostrar la observacion -->

    <ModalObservacion
      titulo="Observación"
      :mensaje="mensajeObservacion"
      :modalvisible="dialogObservacion"
      @confirmar="submitModalObservacion"
    />

  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { CONSTANTS } from './constants/constants'
import { getEtapaProceso, deleteEtapa, getListEtapas, updateEtapa, createEtapa } from '@/api/procesosDIEG/etapas'
import elDragDialog from '@/directive/el-drag-dialog' // base on element-ui
import ModalAgregar from '@/components/ModalAgregar'
import ModalDelete from '@/components/ModalConfirm'
import ModalObservacion from '@/components/ModalConfirm'

export default {
  name: 'EtapasProceso',
  directives: { elDragDialog },
  components: { ModalDelete, ModalAgregar, ModalObservacion },
  props: {
    editar: {
      type: Boolean,
      default: false
    },
    idproceso: {
      type: String,
      default: ''
    },
    recargarlista: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      loadingEtapas: true,
      etapas: [],
      mensajeModalDelete: '',
      deleteDialogVisible: false,
      delEtapa: '',
      delNumeroActo: '',
      formItem: CONSTANTS.formItem,
      domItem: CONSTANTS.domItem,
      rulesFormItem: CONSTANTS.rulesFormItem,
      dataFormItem: CONSTANTS.dataFormItem,
      /* Si es o no visible el cuadro de dialogo de agregar o editar etapa */
      dialogVisibleItem: false,
      tituloModalItem: '',
      modalAction: '',
      drawVisible: false,
      dataActos: {},
      dialogObservacion: false,
      mensajeObservacion: ''
    }
  },
  computed: {
    ...mapGetters(['name', 'roles', 'idusuario', 'dependencia'])
  },
  watch: {
    recargarlista: {
      deep: true,
      handler(val) {
        // console.log('Actualizar lista -> ', val)
        if (val) {
          this.initView()
        }
      }
    }
  },
  async mounted() {
    this.formItem = {} // Permite inicializar el modelo que utiliza el modal de agregar
  },
  created() {
    this.initView()
  },
  methods: {
    openDialogObservacion(msj) {
      this.mensajeObservacion = msj
      this.dialogObservacion = true
    },
    async initView() {
      this.getEtapasProceso(this.idproceso) // Funcion para obtener las etapas del proceso
      this.getEtapas()
    },
    async getEtapasProceso(idproceso) {
      this.loadingEtapas = true
      await getEtapaProceso(idproceso).then((response) => {
        // console.log('ETAPA_PROCESO -> ', response)
        this.etapas = response
        this.loadingEtapas = false
      })
    },
    async getEtapas() {
      await getListEtapas().then((response) => {
        // console.log('Etapas --> ', response)
        this.dataFormItem.etapa = response
      })
    },
    handleEditarEtapa(etapa) {
      // console.log('Editar etapa --> ', etapa)
      this.domItem[0]['disabled'] = true // Se modifican las opciones del select
      this.rulesFormItem['etapa'][0]['required'] = false // Se modifican las reglas del select
      this.getEtapas() // Se actualiza la lista de etapas
      this.formItem = etapa
      this.tituloModalItem = 'Editar etapa'
      this.modalAction = 'Editar'
      this.dialogVisibleItem = true
    },
    async handleConfirmar(modal) { // Funcion que captura los eventos que devuelve el modal de [editar / agregar] etapa
      // console.log(modal)
      if (modal.action === 'Editar') {
        // Se realiza la acción de editar etapa
        modal.data.idproceso = parseInt(this.idproceso)
        await updateEtapa(modal.data).then(async(response) => {
          // console.log('RESPONSE AGREGAR -> ', response)
          this.$notify({
            title: 'Buen trabajo!',
            message: 'Etapa modificada con éxito',
            type: 'success',
            duration: 2000
          })
        })
      } else if (modal.action === 'Agregar') {
        // Se realiza la acción de crear etapa
        modal.data.idproceso = parseInt(this.idproceso)
        await this.getNumeroacto(this.idproceso, modal.data.etapa).then((res) => { modal.data.numeroacto = res })
        await createEtapa(modal.data).then(async(response) => {
          // console.log('RESPONSE AGREGAR -> ', response)
          this.$notify({
            title: 'Buen trabajo!',
            message: 'Etapa agregada con éxito',
            type: 'success',
            duration: 2000
          })
        })
      }
      this.dialogVisibleItem = false
      this.formItem = {} // Se reinicia el modelo del modal (importante)
      this.dataFormItem.etapa = [] // Permite reiniciar el arreglo de etapas del modal (Debido a que los datos quedan cacheados)
      this.getEtapasProceso(this.idproceso) // Se actualiza la lista de etapas
    },
    async getNumeroacto(idproceso, idetapa) {
      let numeroacto = 0
      await getEtapaProceso(idproceso, idetapa).then((response) => {
        // console.log('ETAPA_PROCESO -> ', response)
        if (response.length) {
          // console.log('tiene actos')
          numeroacto = response.length + 1
        } else {
          // console.log('No tiene actos')
          numeroacto = 1
        }
      })
      return numeroacto
    },
    async handleBorrarEtapa(etapa) {
      // console.log('Borrar etapa --> ', etapa)
      this.delEtapa = etapa.etapa
      this.delNumeroActo = etapa.numeroacto
      this.mensajeModalDelete = `¿Realmente desea eliminar la etapa <b>${etapa.nombre}</b>?`
      this.deleteDialogVisible = true
    },
    async submitDelete(response) {
      // console.log(response)
      if (response) {
        const model = { idproceso: this.idproceso, etapa: this.delEtapa, numeroacto: this.delNumeroActo }
        await deleteEtapa(model).then(async(response) => {
          this.$notify({
            title: 'Información',
            message: 'Se ha eliminado la etapa',
            type: 'success',
            duration: 2000
          })
        })
        this.getEtapasProceso(this.idproceso)
      }
      this.deleteDialogVisible = false
    },
    async submitModalObservacion() {
      this.dialogObservacion = false
    },
    handleAgregarActo(acto) {
      console.log('Agregar acto --> ', acto)
      this.domItem[0]['disabled'] = true // Se modifican las opciones del select (con el fin de no modificar el componente de agregar)
      this.rulesFormItem['etapa'][0]['required'] = false // Se modifican las reglas del select
      this.getEtapas() // Se actualiza la lista de etapas
      this.formItem.etapa = acto['actos'][0]['etapa']
      const cantidadactos = acto['actos'].length
      const consecutivoactos = acto['actos'][cantidadactos - 1]['numeroacto']
      this.tituloModalItem = `Agregar acto # ${consecutivoactos + 1}`
      this.modalAction = 'Agregar'
      this.dialogVisibleItem = true
    },
    handleDetalleEtapa(etapa) {
      console.log('Detalle etapa --> ', etapa)
      this.drawVisible = true
      this.dataActos = etapa
    },
    closeDrawer() {
      this.drawVisible = false
      this.getEtapasProceso(this.idproceso)
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

  .control-modal {
    width: 100%;
  }

  .bottom {
    position: absolute;
    bottom: 0%;
    border: 0px solid;
    text-align: center;
    padding: 2%;
    background: #F2F6FC;
  }

  // Pantallas superiores a 800px (PC)
  @media screen and (min-width: 800px) {
    .header-agregar-etapa {
      border: 0px solid;
      width: 100%;
      padding-left: 60px;
      padding-right: 60px;
      padding-bottom: 25px;
      overflow-y: scroll;
      height: 90vh;
    }

    .div-acto {
      height: 18em;
    }
  }

  // Pantallas inferiores a 800px (mobile)
  @media screen and (max-width: 800px) {
    .header-agregar-etapa {
      border: 0px solid;
      width: 100%;
      overflow-y: scroll;
      height: 90vh;
    }

    .div-acto {
      height: 16em;
    }
  }
</style>

<style lang="scss">
  .card-etapa .el-card__header {
    padding: 0;
  }

  .card-etapa .el-card__body {
    padding: 0;
  }

  .card-actuaciones .el-card__body {
    border: 0px solid;
    padding-top: 4%;
    padding-left: 3%;
  }
</style>
