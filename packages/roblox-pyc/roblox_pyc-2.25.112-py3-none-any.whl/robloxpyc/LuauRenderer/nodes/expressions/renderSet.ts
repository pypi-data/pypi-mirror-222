import luau from "../../../LuauAST";
import { render, RenderState } from "../../../LuauRenderer";

export function renderSet(state: RenderState, node: luau.Set) {
	if (luau.list.isEmpty(node.members)) {
		return "{}";
	}

	let result = "{\n";
	state.block(() => {
		luau.list.forEach(node.members, member => (result += state.line(`[${render(state, member)}] = true,`)));
	});
	result += state.indented("}");
	return result;
}
