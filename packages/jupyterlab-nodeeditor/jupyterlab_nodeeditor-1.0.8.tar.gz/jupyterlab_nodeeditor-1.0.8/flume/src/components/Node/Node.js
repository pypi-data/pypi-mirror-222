import React from "react";
import styles from "./Node.css";
import {
  NodeTypesContext,
  NodeDispatchContext,
  StageContext,
  CacheContext,
  OwnerContext,
} from "../../context";
import { getPortRect, calculateCurve } from "../../connectionCalculator";
import { Portal } from "react-portal";
import ContextMenu from "../ContextMenu/ContextMenu";
import IoPorts from "../IoPorts/IoPorts";
import Draggable from "../Draggable/Draggable";

const Node = ({
  id,
  width,
  x,
  y,
  stageRect,
  connections,
  type,
  inputData,
  root,
  onDragStart,
  renderNodeHeader,
}) => {
  const owner = React.useContext(OwnerContext);
  const cache = React.useContext(CacheContext);
  const nodeTypes = React.useContext(NodeTypesContext);
  const nodesDispatch = React.useContext(NodeDispatchContext);
  const stageState = React.useContext(StageContext);
  const currentNodeType = nodeTypes[type];
  const { label, deletable, inputs = [], outputs = [] } = currentNodeType;

  const nodeWrapper = React.useRef();
  const [menuOpen, setMenuOpen] = React.useState(false);
  const [menuCoordinates, setMenuCoordinates] = React.useState({ x: 0, y: 0 });

  const byScale = value => (1 / stageState.scale) * value;

  const updateConnectionsByTransput = (transput = {}, isOutput) => {
    for (const portName in transput) {
      let outputs = transput[portName]
      for (const output of outputs) {
        const toRect = getPortRect(
          id,
          portName,
          isOutput ? "output" : "input",
          cache
        );
        const fromRect = getPortRect(
          output.nodeId,
          output.portName,
          isOutput ? "input" : "output",
          cache
        );
        const portHalf = fromRect.width / 2;
        let combined;
        if (isOutput) {
          combined = id + portName + output.nodeId + output.portName;
        } else {
          combined = output.nodeId + output.portName + id + portName;
        }
        let cnx;
        const cachedConnection = cache.current.connections[combined];
        if (cachedConnection) {
          cnx = cachedConnection;
        } else {
          cnx = document.querySelector(`[data-connection-id="${combined}"]`);
          cache.current.connections[combined] = cnx;
        }
        const from = {
          x:
            byScale(
              toRect.x -
              stageRect.current.x +
              portHalf -
              stageRect.current.width / 2
            ) + byScale(stageState.translate.x),
          y:
            byScale(
              toRect.y -
              stageRect.current.y +
              portHalf -
              stageRect.current.height / 2
            ) + byScale(stageState.translate.y)
        };
        const to = {
          x:
            byScale(
              fromRect.x -
              stageRect.current.x +
              portHalf -
              stageRect.current.width / 2
            ) + byScale(stageState.translate.x),
          y:
            byScale(
              fromRect.y -
              stageRect.current.y +
              portHalf -
              stageRect.current.height / 2
            ) + byScale(stageState.translate.y)
        };
        cnx.setAttribute("d", calculateCurve(from, to));
      }
    }

  };

  const updateNodeConnections = () => {
    if (connections) {
      updateConnectionsByTransput(connections.inputs);
      updateConnectionsByTransput(connections.outputs, true);
    }
  };

  const stopDrag = (e, coordinates) => {
    nodesDispatch({
      type: "SET_NODE_COORDINATES",
      ...coordinates,
      nodeId: id
    });
  };

  const handleDrag = ({ x, y }) => {
    nodeWrapper.current.style.transform = `translate(${x}px,${y}px)`;
    updateNodeConnections();
  };

  const startDrag = e => {
    onDragStart();
    onNodeStartDrag()
  };

  const handleContextMenu = e => {
    e.preventDefault();
    e.stopPropagation();
    setMenuCoordinates({ x: e.clientX, y: e.clientY });
    setMenuOpen(true);
    return false;
  };

  const closeContextMenu = () => {
    setMenuOpen(false);
  };

  const deleteNode = () => {
    nodesDispatch({
      type: "REMOVE_NODE",
      nodeId: id
    });
  };

  const handleMenuOption = ({ value }) => {
    switch (value) {
      case "deleteNode":
        deleteNode();
        break;
      case "runNode":
        if (owner && owner.runNode) {
          owner.runNode(id)
        }
        break;
      default:
        return;
    }
  };

  const onMouseDown = (e) => {
    if (owner && owner.onNodeMouseDown) {
      owner.onNodeMouseDown(e, id, nodeWrapper.current)
    }
  }

  const onMouseUp = (e) => {
    if (owner && owner.onNodeMouseUp) {
      owner.onNodeMouseUp(e, id, nodeWrapper.current)
    }
  }

  const onNodeStartDrag = () => {
    if (owner && owner.onNodeStartDrag) {
      owner.onNodeStartDrag(id, nodeWrapper.current)
    }
  }

  const startDragDelayRef = React.useRef(null)

  if (owner && owner.outOptions) {
    owner.outOptions({
      [`updateNodeConnections_${id}`]: updateNodeConnections,
      [`nodeDraggable_${id}`]: nodeWrapper,
      [`startDragDelay_${id}`]: startDragDelayRef
    })
  }

  return (
    <Draggable
      className={styles.wrapper}
      style={{
        width,
        transform: `translate(${x}px, ${y}px)`
      }}
      onDragStart={startDrag}
      onDrag={handleDrag}
      onDragEnd={stopDrag}
      innerRef={nodeWrapper}
      id={id}
      data-node-id={id}
      data-flume-component="node"
      data-flume-node-type={currentNodeType.type}
      data-flume-component-is-root={!!root}
      onContextMenu={handleContextMenu}
      stageState={stageState}
      stageRect={stageRect}
      onMouseDown={onMouseDown}
      onMouseUp={onMouseUp}
      startDragDelayRef={startDragDelayRef}
    >
      {renderNodeHeader ? (
        renderNodeHeader(NodeHeader, currentNodeType, {
          openMenu: handleContextMenu,
          closeMenu: closeContextMenu,
          deleteNode
        }, id)
      ) : (
        <NodeHeader>{label}</NodeHeader>
      )}
      <IoPorts
        nodeId={id}
        inputs={inputs}
        outputs={outputs}
        connections={connections}
        updateNodeConnections={updateNodeConnections}
        inputData={inputData}
      />
      {/* {menuOpen ? (
        <Portal>
          <ContextMenu
            x={menuCoordinates.x}
            y={menuCoordinates.y}
            options={[
              ...(deletable !== false
                ? [
                  {
                    label: "删除(Delete)",
                    value: "deleteNode",
                    description: "Deletes a node and all of its connections."
                  }
                ]
                : []),
              {
                label: "运行(Run)",
                value: "runNode",
                description: "运行该节点"
              }
            ]}
            onRequestClose={closeContextMenu}
            onOptionSelected={handleMenuOption}
            hideFilter
            label="Node Options"
            emptyText="This node has no options."
            from="node"
          />
        </Portal>
      ) : null} */}
    </Draggable>
  );
};

const NodeHeader = ({ children, className = "", ...props }) => (
  <h2 {...props} className={styles.label + (className ? ` ${className}` : "")} data-flume-component="node-header">
    {children}
  </h2>
);

export default Node;
