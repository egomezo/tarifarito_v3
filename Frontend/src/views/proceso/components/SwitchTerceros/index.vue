<template>
  <el-col :md="24" style="border: 0px solid blue; padding-top: 10px;">
    <el-card>
      <el-row>
        <el-col :md="countTerceros > 0 ? 22 : 22">
          <span>{{ title }}</span>
        </el-col>
        <el-col :md="countTerceros > 0 ? 0 : 2">
          <el-switch v-show="countTerceros > 0 ? false : true" v-model="valSwitch" active-color="#13ce66" />
        </el-col>
        <el-col v-show="countTerceros > 0" :md="countTerceros > 0 ? 2 : 0">
          <div class="badge-tercero">
            <el-badge :value="countTerceros" class="item" type="success">
              <el-link icon="el-icon-message-solid" :underline="false" @click="dialogDrawer = true" />
            </el-badge>
          </div>
        </el-col>
      </el-row>
    </el-card>

    <!-- Cuadro de dialogo para agregar tercero -->

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

    <ListaTerceros
      drawertitulo="Terceros interesados"
      :dialogdrawer="dialogDrawer"
      :dataterceros="terceros"
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
import ListaTerceros from './ListaTerceros'
import { getTercerosProceso, createTercero } from '@/api/procesosDIEG/terceros'

export default {
  directives: { },
  components: { ModalAgregar, ListaTerceros },
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
      countTerceros: 0,
      dialogVisible: false,
      tituloModalItem: '',
      formItem: CONSTANTS.formItem,
      domItem: CONSTANTS.domItem,
      rulesFormItem: CONSTANTS.rulesFormItem,
      dataFormItem: CONSTANTS.dataFormItem,
      modalAction: '',
      dialogDrawer: false,
      terceros: [],
      cantidadCausasProceso: []
    }
  },
  watch: {
    valSwitch: {
      deep: true,
      handler(val) {
        // console.log('valSwitch - > ', val)
        if (this.countTerceros > 0) {
          this.valSwitch = true
          this.switchDisable = true
        } else {
          this.switchDisable = false
          this.valSwitch = false
          if (!this.dialogDrawer) {
            this.dialogVisible = true
            this.modalAction = 'Agregar'
            this.tituloModalItem = 'Agregar tercero'
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
      this.getTerceros()
    },
    handleUpdateView() {
      this.getTerceros()
    },
    async getTerceros() {
      await getTercerosProceso(this.idproceso).then((response) => {
        // console.log('TERCEROS -> ', response)
        this.countTerceros = response.length
        if (response.length) {
          this.terceros = response
        } else {
          this.dialogDrawer = false
        }
      })
    },
    handleClose(resp) {
      // console.log('cerrar drawer ->> ', resp)
      this.dialogDrawer = resp
      // this.$destroy()
    },
    async handleConfirmar(modal) { // Funcion que captura los eventos que devuelve el modal de [editar / agregar] tercero
      // console.log(modal)
      if (modal.action === 'Agregar') {
        // console.log(modal)
        modal.data.idproceso = parseInt(this.idproceso)
        modal.data.persona = this.dataFormItem.persona.find((persona) => persona.label === modal.data.persona).id
        await createTercero(modal.data).then(async(response) => {
          this.$notify({
            title: 'Buen trabajo!',
            message: 'Tercero agregado con éxito',
            position: 'bottom-right',
            type: 'success',
            duration: 2000
          })
        }, (err) => {
          console.log(err)
          this.$notify({
            title: 'Advertencia',
            message: 'Documento de usuario ya registrado!',
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
